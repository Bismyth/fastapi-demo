<script setup lang="ts">
import type { User, UserError } from '@/api/user'

defineProps<{ users: User[] }>()

const emit = defineEmits<{
  (e: 'create'): void
  (e: 'edit', id: User['id']): void
  (e: 'change'): void
  (e: 'error', msg: string): void
}>()

const deleteUser = async (id: User['id']) => {
  const response = await fetch(`/api/users/${id}`, { method: 'delete' })

  if (response.ok) {
    emit('change')
  }

  const msg = (await response.json()) as UserError
  emit('error', msg.detail)
}
</script>

<template>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th><a @click="emit('create')">Add</a></th>
        <th>Id</th>
        <th>Username</th>
        <th>Email</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user.id">
        <td><a @click="emit('edit', user.id)">Edit</a></td>
        <td>{{ user.id }}</td>
        <td>{{ user.username }}</td>
        <td>{{ user.email }}</td>
        <td><a @click="deleteUser(user.id)">Delete</a></td>
      </tr>
    </tbody>
  </table>
</template>
