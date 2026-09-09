<script setup lang="ts">
withDefaults(defineProps<{ padding?: string }>(), { padding: 'p-6' })
</script>

<template>
  <div class="glass rounded-2xl" :class="padding">
    <slot />
  </div>
</template>
