<script setup lang="ts">
import type { User, UserError } from '@/api/user'
import { reactive, ref } from 'vue'

const emit = defineEmits<{
  (e: 'change'): void
  (e: 'error', msg: string): void
}>()

const shown = ref(false)

const formData = reactive<Partial<User>>({})

const newEntry = ref(true)

const showForm = async (id?: User['id']) => {
  newEntry.value = id === undefined

  if (!newEntry.value) {
    const response = await fetch(`/api/users/${id}`)
    const user = await response.json()
    Object.assign(formData, user)
  } else {
    Object.assign(formData, { username: '', email: '', id: undefined })
  }

  shown.value = true
}

const close = () => {
  shown.value = false
}

const submit = async () => {
  let method = 'POST'
  let url = '/api/users'
  if (!newEntry.value) {
    method = 'PUT'
    url += `/${formData.id}`
  }
  console.log(JSON.stringify(formData))
  const response = await fetch(url, {
    method,
    body: JSON.stringify(formData),
    headers: { 'Content-Type': 'application/json' }
  })
  if (response.ok) {
    shown.value = false
    emit('change')
  }

  const errData = (await response.json()) as UserError

  emit('error', errData.detail)
}

defineExpose({ showForm, close })
</script>

<template>
  <div class="modal" :class="{ 'is-active': shown }">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">{{ newEntry ? 'Create' : 'Edit' }} User</p>
        <button class="delete" aria-label="close" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <form>
          <div class="field">
            <label class="label">Username</label>
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="Username..."
                v-model="formData.username"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input class="input" type="text" placeholder="Email..." v-model="formData.email" />
            </div>
          </div>
        </form>
      </section>
      <footer class="modal-card-foot">
        <slot name="footer">
          <div class="buttons">
            <button class="button" @click="close">Close</button>
            <button class="button is-link" @click="submit">
              {{ newEntry ? 'Create' : 'Save' }}
            </button>
          </div>
        </slot>
      </footer>
    </div>
  </div>
</template>
