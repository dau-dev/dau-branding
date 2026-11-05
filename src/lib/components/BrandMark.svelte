<script lang="ts">
  interface Props {
    href?: string;
  }

  let { href = '/' }: Props = $props();
</script>

<a {href}><span aria-hidden="true">D</span>dau</a>

<style>
  a {
    display: inline-flex;
    align-items: center;
    gap: 0.625rem;
    color: inherit;
    font-weight: 700;
    text-decoration: none;
  }

  span {
    display: grid;
    width: 2rem;
    height: 2rem;
    place-items: center;
    border-radius: 50%;
    color: var(--dau-bg);
    background: var(--dau-fg);
  }
</style>
