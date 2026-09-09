<script setup lang="ts">
import { Download } from '@lucide/vue'
import BrandIcon from './BrandIcon.vue'
import contato from '../data/contato.json'
import brandIcons from '../data/brand-icons.json'
</script>

<template>
  <footer class="glass mt-16">
    <div class="max-w-6xl mx-auto px-4 py-10 grid gap-6 md:grid-cols-3 text-sm">
      <div>
        <p class="font-bold text-brand-dark text-base mb-1">Daniel de Oliveira</p>
        <p class="text-brand-dark/60">IA aplicada, automação e produtos digitais com impacto real.</p>
        <p class="text-brand-dark/40 text-xs mt-2">CTO · pesquisador · professor</p>
      </div>
      <div>
        <p class="font-bold text-brand-dark mb-2">Contato direto</p>
        <div class="flex flex-col gap-1.5">
          <a :href="contato.whatsappLink" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-brand-dark/70 hover:text-brand-dark font-medium">
            <BrandIcon :path="brandIcons.whatsapp.path" :hex="brandIcons.whatsapp.hex" label="WhatsApp" /> {{ contato.whatsappDisplay }}
          </a>
          <a :href="`mailto:${contato.email}`" class="inline-flex items-center gap-2 text-brand-dark/70 hover:text-brand-dark font-medium">
            <BrandIcon :path="brandIcons.gmail.path" :hex="brandIcons.gmail.hex" label="Gmail" /> {{ contato.email }}
          </a>
          <a :href="contato.cvUrl" class="inline-flex items-center gap-2 text-brand-dark/70 hover:text-brand-dark font-medium">
            <Download class="w-4 h-4 text-brand-green" /> Baixar CV
          </a>
        </div>
      </div>
      <div>
        <p class="font-bold text-brand-dark mb-2">Perfis</p>
        <div class="flex flex-col gap-1.5">
          <a :href="contato.linkedinUrl" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-brand-dark/70 hover:text-brand-dark font-medium">
            <BrandIcon :path="brandIcons.linkedin.path" :hex="brandIcons.linkedin.hex" label="LinkedIn" /> LinkedIn
          </a>
          <a :href="contato.githubUrl" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-brand-dark/70 hover:text-brand-dark font-medium">
            <BrandIcon :path="brandIcons.github.path" label="GitHub" class="brand-github" /> GitHub
          </a>
          <a :href="contato.lattesUrl" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-brand-dark/70 hover:text-brand-dark font-medium">
            <BrandIcon :path="brandIcons.lattes.path" :hex="brandIcons.lattes.hex" :viewBox="brandIcons.lattes.viewBox" label="Lattes" /> Lattes
          </a>
        </div>
      </div>
    </div>
    <div class="border-t border-brand-green/10 py-4 text-center text-xs text-brand-dark/50">
      <p>&copy; {{ new Date().getFullYear() }} Daniel de Oliveira. Todos os direitos reservados.</p>
    </div>
  </footer>
</template>
