# motion/ — Placeholder (v0.2 stub only)

> This directory is reserved for Lottie / Rive / CSS-keyframe presets.
> **v0.2 ships the stub only.** Actual motion presets are deferred to a later release
> because real-world demand evidence is currently zero (see B2 §5.3, R2 13-case audit).

## When `medium: motion` is detected

`insane-build` Step 0 should:
1. Detect `medium: motion` in `design.md` frontmatter.
2. Read this file.
3. Output this guidance to the user (Korean):
   ```
   📦 motion 프리셋은 v0.2에 스텁만 포함되어 있습니다.
   현재는 design.md §10 Motion을 참고해 CSS keyframe을 직접 작성하거나,
   Lottie/Rive 파일을 수동으로 임베드하세요.
   다음 버전(v0.3+)에서 Lottie JSON + Rive .riv 로더 프리셋을 추가할 예정입니다.
   ```
4. Fall through to `web/` scaffolds as the underlying frame.

## Future scope (deferred)

- `lottie-hero.html` — Lottie JSON-driven hero animation shell
- `rive-interactive.html` — Rive `.riv` + state machine binding
- `css-keyframes.html` — Pure CSS timeline (staggered reveal, scroll-triggered)

No code in this directory yet. Do not invent one.
