<script setup lang="ts">
import { useFetch } from '@/utils/fetch'
import type { ComponentExposed } from 'vue-component-type-helpers'
import { onMounted, ref } from 'vue'
import type { User } from '@/api/user'
import UserTable from '@/components/UserTable.vue'
import UserForm from '@/components/UserForm.vue'

const { data: users, loading, load } = useFetch<User[]>('/api/users/', { initialFetch: false })

onMounted(() => {
  load()
})

const formRef = ref<ComponentExposed<typeof UserForm> | null>(null)

const createUser = () => {
  formRef.value?.showForm(undefined)
}

const editUser = (id: User['id']) => {
  formRef.value?.showForm(id)
}
</script>

<template>
  <main>
    <div class="container">
      <h1 class="title mt-5">Users</h1>
      <span v-if="loading">Loading...</span>
      <UserTable :users="users ?? []" @change="load()" @create="createUser" @edit="editUser" />
      <UserForm ref="formRef" @change="load()" />
    </div>
  </main>
</template>
