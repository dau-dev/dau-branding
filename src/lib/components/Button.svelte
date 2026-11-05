<script lang="ts">
  import type { Snippet } from 'svelte';

  interface Props {
    /** Renders a link when set, a button otherwise. */
    href?: string;
    variant?: 'primary' | 'secondary';
    size?: 'md' | 'sm';
    type?: 'button' | 'submit';
    onclick?: (event: MouseEvent) => void;
    children: Snippet;
    [key: `data-${string}`]: string | undefined;
  }

  let { href, variant = 'primary', size = 'md', type = 'button', onclick, children, ...rest }: Props = $props();
</script>

{#if href}
  <a class="btn {variant} {size}" {href} {...rest}>{@render children()}</a>
{:else}
  <button class="btn {variant} {size}" {type} {onclick} {...rest}>{@render children()}</button>
{/if}

<style>
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5em;
    border: 1px solid var(--dau-fg);
    border-radius: 0;
    font-family: var(--dau-font-sans);
    font-weight: 600;
    line-height: 1.2;
    text-decoration: none;
    cursor: pointer;
  }

  .md {
    padding: 0.75rem 1.25rem;
    font-size: 1rem;
  }

  .sm {
    padding: 0.4rem 0.8rem;
    font-size: 0.875rem;
  }

  .primary {
    color: var(--dau-bg);
    background: var(--dau-fg);
  }

  .primary:hover {
    color: var(--dau-fg);
    background: transparent;
  }

  .secondary {
    color: var(--dau-fg);
    background: transparent;
  }

  .secondary:hover {
    background: var(--dau-bg-raised);
  }
</style>
