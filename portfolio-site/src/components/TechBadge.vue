<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  path?: string
  hex?: string
  label: string
}>()

const color = computed(() => (props.hex ? `#${props.hex}` : '#518E45'))
</script>

<template>
  <span
    class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full glass text-xs font-medium text-brand-dark/80"
    :title="label"
  >
    <svg
      v-if="path"
      viewBox="0 0 24 24"
      class="w-4 h-4 shrink-0"
      fill="currentColor"
      :style="{ color }"
    >
      <path :d="path" />
    </svg>
    <span>{{ label }}</span>
  </span>
</template>