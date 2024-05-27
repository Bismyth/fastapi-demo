import { ref } from 'vue'

interface CustomFetchOptions {
  initialFetch: boolean
}

export const useFetch = <T>(url: string, options?: RequestInit & CustomFetchOptions) => {
  const data = ref<T | null>(null)
  const loading = ref(true)

  const load = async (options?: RequestInit) => {
    const response = await fetch(url, options)
    data.value = await response.json()
    if (loading.value) {
      loading.value = false
    }
  }
  if (options?.initialFetch) {
    load(options)
  }

  return { data, loading, load }
}
