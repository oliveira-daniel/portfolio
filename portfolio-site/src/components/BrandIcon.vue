<script setup lang="ts">
withDefaults(
  defineProps<{
    path: string
    hex?: string
    label?: string
    viewBox?: string
  }>(),
  { viewBox: '0 0 24 24' },
)
</script>

<template>
  <svg
    :viewBox="viewBox"
    class="w-4 h-4 shrink-0"
    fill="currentColor"
    :style="hex ? { color: `#${hex}` } : undefined"
    role="img"
    :aria-label="label"
  >
    <path :d="path" />
  </svg>
</template>
