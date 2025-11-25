
```
┌─────────────────────────────┐
│     GitHub Organization     │
└─────────────────────────────┘
        │
        ├── People
        │       ├── members
        │       │
        │       │
        │       └── outside-collaborators
        │
        │
        │
        └── Repositories
                ├── repo-a (private)
                │     → 仅members可见
                │     → GitHub Pages不可用
                │       需要升级到GitHub Enterprise
                │       可以隐私发布网页, 使得仅members可见
                │
                └── repo-b (Public)
                      → 所有人可见
                      → 可以选择启用GitHub Pages
```

```
jiayong-yu ─────────●──修改1提交──push──●
                    ↑                   │
                    | merge             | create pull request & Handled by the person in charge
                    |                   |
main ──────●─●──────●───────────────────●─────────────────────────────●───►
                                        |                             │
                                        │ merge                       │ create pull request & Handled by the person in charge
                                        ↓                             │
yun-xu ─────────────────────────────────●──修改1提交──修改2提交──push──●
```
