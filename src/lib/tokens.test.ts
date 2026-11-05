import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

const css = readFileSync('src/lib/styles/tokens.css', 'utf8');

function block(selector: string): Record<string, string> {
  const start = css.indexOf(selector);
  const body = css.slice(css.indexOf('{', start) + 1, css.indexOf('}', start));
  return Object.fromEntries([...body.matchAll(/--([\w-]+):\s*(#[0-9a-f]{6})/gi)].map((m) => [m[1], m[2]]));
}

function luminance(hex: string): number {
  const channel = (i: number) => {
    const c = parseInt(hex.slice(i, i + 2), 16) / 255;
    return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
  };
  return 0.2126 * channel(1) + 0.7152 * channel(3) + 0.0722 * channel(5);
}

function contrast(a: string, b: string): number {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
}

describe.each([
  ['lit', ':root,\n.dau-lit'],
  ['shadow', ":root[data-theme='dark'],\n.dau-shadow"]
])('%s surface', (_name, selector) => {
  const t = block(selector);

  it.each(['dau-bg', 'dau-bg-raised'])('text meets AA on %s', (surface) => {
    expect(contrast(t['dau-fg'], t[surface])).toBeGreaterThanOrEqual(4.5);
    expect(contrast(t['dau-fg-muted'], t[surface])).toBeGreaterThanOrEqual(4.5);
  });

  it('focus ring meets 3:1', () => {
    expect(contrast(t['dau-focus'], t['dau-bg'])).toBeGreaterThanOrEqual(3);
  });
});
