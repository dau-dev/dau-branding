# @dau/branding

dau brand identity, design tokens, theme system, and reusable Svelte components.

See [`BRAND.md`](./BRAND.md) for the canonical brand guide.

## Install

```bash
pnpm add @dau/branding
```

Import design tokens once at the application root:

```css
@import '@dau/branding/tokens.css';
```

```svelte
<script lang="ts">
  import { BrandMark, ThemeToggle } from '@dau/branding';
</script>

<BrandMark />
<ThemeToggle />
```

## Develop

```bash
pnpm install
pnpm dev
pnpm check
pnpm lint
pnpm fix
pnpm test
pnpm build
```

After customizing the showcase, run `pnpm test:e2e:update` once to establish its visual baseline.
