import { defineConfig } from 'vitepress'

const siteUrl = 'https://4k4m1m3-org.github.io/ResumeSpec/'
const repoUrl = 'https://github.com/4k4m1m3-org/ResumeSpec'
const releaseUrl = 'https://github.com/4k4m1m3-org/ResumeSpec/releases/tag/v1.0.0'

function getPageUrl(relativePath: string): string {
  const path = relativePath
    .replace(/\.md$/, '')
    .replace(/(^|\/)index$/, '$1')

  return `${siteUrl}${path}`
}

export default defineConfig({
  lang: 'en-US',
  title: 'ResumeSpec',
  description:
    'An open standard for representing professional identity as structured, portable, machine-readable data.',
  base: '/ResumeSpec/',
  cleanUrls: true,
  appearance: true,
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', href: '/ResumeSpec/favicon.svg', type: 'image/svg+xml' }],
    ['meta', { property: 'og:site_name', content: 'ResumeSpec' }],
    ['meta', { property: 'og:title', content: 'ResumeSpec — One professional identity. Unlimited representations.' }],
    ['meta', { property: 'og:description', content: 'An open standard for representing professional identity as structured, portable, machine-readable data.' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:image', content: `${siteUrl}banner.png` }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'ResumeSpec — One professional identity. Unlimited representations.' }],
    ['meta', { name: 'twitter:description', content: 'An open standard for representing professional identity as structured, portable, machine-readable data.' }],
    ['meta', { name: 'twitter:image', content: `${siteUrl}banner.png` }],
    ['meta', { name: 'theme-color', content: '#0f172a' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap' }],
    ['meta', { name: 'robots', content: 'index,follow' }],
  ],
  transformHead({ pageData }) {
    const pageUrl = getPageUrl(pageData.relativePath)

    return [
      ['link', { rel: 'canonical', href: pageUrl }],
      ['meta', { property: 'og:url', content: pageUrl }],
    ]
  },
  themeConfig: {
    siteTitle: 'ResumeSpec',
    logo: '/favicon.svg',
    nav: [
      { text: 'Get Started', link: '/get-started/' },
      { text: 'Specification', link: '/specification/' },
      { text: 'Reference', link: '/reference/' },
      { text: 'Examples', link: '/examples/' },
      { text: 'Community', link: '/community/' },
    ],
    sidebar: {
      '/get-started/': [
        {
          text: 'Get Started',
          items: [
            { text: 'Introduction', link: '/get-started/introduction' },
            { text: 'Quick Start', link: '/get-started/quick-start' },
            { text: 'Core Concepts', link: '/get-started/core-concepts' },
          ],
        },
      ],
      '/specification/': [
        {
          text: 'Specification',
          items: [
            { text: 'Overview', link: '/specification/' },
            { text: 'Data Model', link: '/specification/data-model' },
            { text: 'JSON Schema', link: '/specification/json-schema' },
            { text: 'Formats', link: '/specification/formats' },
            { text: 'Versioning', link: '/specification/versioning' },
          ],
        },
      ],
      '/reference/': [
        {
          text: 'Reference',
          items: [
            { text: 'Python', link: '/reference/python' },
            { text: 'Parser', link: '/reference/parser' },
            { text: 'Validator', link: '/reference/validator' },
            { text: 'CLI', link: '/reference/cli' },
          ],
        },
      ],
      '/examples/': [
        {
          text: 'Examples',
          items: [
            { text: 'JSON', link: '/examples/json' },
            { text: 'YAML', link: '/examples/yaml' },
            { text: 'XML', link: '/examples/xml' },
          ],
        },
      ],
      '/community/': [
        {
          text: 'Community',
          items: [
            { text: 'Contributing', link: '/community/contributing' },
            { text: 'Roadmap', link: '/community/roadmap' },
            { text: 'GitHub', link: '/community/github' },
          ],
        },
      ],
    },
    socialLinks: [
      { icon: 'github', link: repoUrl },
      { icon: { svg: '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10s10-4.48 10-10S17.52 2 12 2Zm1 17h-2v-2h2v2Zm1.84-7.45l-.9.92c-.72.73-1.06 1.13-1.06 2.53h-2v-.5c0-1.04.34-1.92 1.06-2.65l1.24-1.26c.37-.36.56-.85.56-1.44c0-1.1-.9-2-2-2s-2 .9-2 2H8a4 4 0 1 1 8 0c0 .92-.36 1.77-1.16 2.38Z"/></svg>' }, link: releaseUrl },
    ],
    footer: {
      message: 'ResumeSpec v1.0.0',
      copyright: 'Open standard, open repository.',
    },
    editLink: {
      pattern: `${repoUrl}/edit/main/site/:path`,
      text: 'Edit this page on GitHub',
    },
    outline: [2, 3],
    search: {
      provider: 'local',
    },
  },
})
