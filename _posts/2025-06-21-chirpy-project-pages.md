---
layout: post
title: "[Chirpy Blog] How to Split Projects into Individual Pages"
categories: [GitHub Blog, Chirpy]
tags: [chirpy, github pages, jekyll, blog]
pin: true
---

Recently, I refactored the "Projects" tab of my GitHub blog using the **Chirpy theme** to make each project its own standalone page instead of displaying all projects in one long scroll. This tutorial outlines the step-by-step process I followed, so you can do it too!

---

## ✅ Goal

Originally, all project descriptions were inside one `/tabs/projects/` page using `<details>` toggles.  
The new structure looks like this:

- `/tabs/projects/` → remains as a summary list with links
- `/projects/project-name/` → new pages for each detailed project

---

## 🪜 Steps to Follow

### 1️⃣ Create `_pages/projects/` Folder

In the root directory of your blog (where `_config.yml` is), create a `_pages/` folder if it doesn't exist.  
Inside that, create a subfolder called `projects`:

```
📁 _pages/
└── 📁 projects/
    ├── battery-swapping.md
    ├── dog-facial-synthesis.md
    ├── ...
```

---

### 2️⃣ Write Each Project Page

For example: `battery-swapping.md`

```markdown
---
layout: page
title: Battery Swapping Station Location Optimization
permalink: /projects/battery-swapping/
---

# Battery Swapping Station Location Optimization

>`Geospatial Data`  
>`XGBoost Regression`  
>`Map Visualization`

(Add your project details here)
```

Ensure that the `permalink` ends with a `/` to work correctly.

---

### 3️⃣ Update `_tabs/projects.md`

This file originally held all your project content. Now, simplify it into a list of links:

```markdown
---
title: Projects
icon: fas fa-project-diagram
order: 3
---

Here are my featured projects 👇

- [🔋 Battery Swapping](/projects/battery-swapping/)
- [🐶 Dog Facial Synthesis](/projects/dog-facial-synthesis/)
- [📚 Policy Knowledge Graph](/projects/policy-kg/)
- [🛠 Welding Defect Detection](/projects/welding-defect/)
- [🔥 Electrode Temperature Forecasting](/projects/electrode-temperature/)
```

---

### 4️⃣ Modify `_config.yml`

Chirpy does not automatically render pages inside `_pages/`, so you must explicitly define the collection:

```yaml
collections:
  pages:
    output: true
    permalink: /:path/
```

Without this, the `_pages/` content won’t render as separate pages.

---

### 5️⃣ Run Your Blog Locally

Use the following commands:

```bash
bundle install
bundle exec jekyll serve
```

Then visit:  
`http://localhost:4000/projects/battery-swapping/`  
to check if the pages work as expected.

---

## 📝 Conclusion

With this setup, your GitHub blog becomes much more organized. Each project gets its own URL and looks cleaner for readers.  
If you have questions or run into trouble, feel free to reach out or leave a GitHub issue.

---

> 💡 I'm using the customized [Chirpy Theme](https://github.com/cotes2020/jekyll-theme-chirpy) for my GitHub Pages blog.
