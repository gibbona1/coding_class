---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
#background: https://cover.sli.dev
background: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
# some information about your slides (markdown enabled)
title: Intro to GitHub
info: |
  ## Slidev Starter Template
  Version control and collaboration platform for developers

# apply unocss classes to the current slide
class: text-center
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# https://sli.dev/guide/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/guide/syntax#mdc-syntax
mdc: true
---

# Intro to GitHub

Version control and collaboration platform for developers

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: slide-left
---

# Table of Contents

1. **What is GitHub**
2. **Setting Up Software**
3. **How it Works**
4. **Example**

<!--
You can have `style` tag in markdown to override the style for the current page.
Learn more: https://sli.dev/guide/syntax#embedded-styles
-->


---
transition: slide-left
---

<div class="absolute top-5 right-5 w-25 h-25">
  <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" />
</div>

# What is GitHub?
(And why is it useful?)

**GitHub** is the most popular online repository for open source projects. 

It uses **Git**, which is the version control system working in the backgrounf that tracks versions of files.

**Developers** (and all kinds of creators) use GitHub for:

- **Code Hosting**: Store and manage code repositories.
- **Collaboration**: Work with others through pull requests, issues, and code reviews.
- **Version Control**: Track and manage changes to code over time.

<!--
comments
-->

---
transition: slide-left
---

# **Setting Up Software**

- Sign up to GitHub with your personal email. https://github.com/signup
- Download GitHub Desktop (available on Windows, Mac and Linux). https://desktop.github.com/download
- Download Git if it isn't automatically installed by the GitHub Destop app. https://git-scm.com/downloads

<div class="flex justify-around items-center h-full">
  <div class="flex flex-col items-center">
<img
  class="w-40 h-40"
  src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
  alt="GitHub"
/>
<p class="mt-4">
  <a href="https://github.com/signup" class="center">GitHub</a>
</p>
</div>

<div class="flex flex-col items-center">
<img
  class="w-40 h-40"
  src="https://desktop.github.com/images/desktop-icon.svg"
  alt="GitHub Desktop"
/>
<p class="mt-4">
  <a href="https://desktop.github.com/download">GitHub Desktop</a>
</p>
</div>

<div class="flex flex-col items-center">
<img
  class="w-40 h-40"
  src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.svg"
  alt="Git"
/>
<p class="mt-4">
  <a href="https://git-scm.com/downloads">Git</a>
</p>
</div>
</div>


---
transition: slide-left
---

# **How it Works**

- Local files
- Local Git repository
- Online (GitHub) repository
- Commits
- Push and Pull

---
transition: slide-left
---

# GitHub Workflow

<div class="flex justify-around items-center h-full">
  <div class="flex flex-col items-center">
    <div class="bg-gray-200 p-4 rounded shadow-md">
      <p>Fake Filesystem</p>
      <ul>
        <li>file1.txt</li>
        <li>file2.txt</li>
        <li>directory/</li>
      </ul>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-blue-200 p-4 rounded-full shadow-md">
      <p>Local Git Repo</p>
    </div>
  </div>
</div>

---
transition: slide-left
---

# GitHub Workflow

<div class="flex justify-around items-center h-full">
  <div class="flex flex-col items-center">
    <div class="bg-gray-200 p-4 rounded shadow-md">
      <p>Fake Filesystem</p>
      <ul>
        <li>file1.txt</li>
        <li>file2.txt</li>
        <li>directory/</li>
      </ul>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-blue-200 p-4 rounded-full shadow-md">
      <p>Local Git Repo</p>
    </div>
  </div>
</div>

<div class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2">
  <p>Commit</p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Arrow_right.svg/2560px-Arrow_right.svg.png" alt="Commit" class="w-32">
</div>


---
transition: slide-left
---

# GitHub Workflow

<div class="flex justify-around items-center h-full">
  <div class="flex flex-col items-center">
    <div class="bg-gray-200 p-4 rounded shadow-md">
      <p>Fake Filesystem</p>
      <ul>
        <li>file1.txt</li>
        <li>file2.txt</li>
        <li>directory/</li>
      </ul>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-blue-200 p-4 rounded-full shadow-md">
      <p>Local Git Repo</p>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-green-200 p-4 rounded-full shadow-md">
      <p>Main GitHub Repo</p>
    </div>
  </div>
</div>


---
transition: slide-left
---

# GitHub Workflow

<div class="flex justify-around items-center h-full">
  <div class="flex flex-col items-center">
    <div class="bg-gray-200 p-4 rounded shadow-md">
      <p>Fake Filesystem</p>
      <ul>
        <li>file1.txt</li>
        <li>file2.txt</li>
        <li>directory/</li>
      </ul>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-blue-200 p-4 rounded-full shadow-md">
      <p>Local Git Repo</p>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-green-200 p-4 rounded-full shadow-md">
      <p>Main GitHub Repo</p>
    </div>
  </div>
</div>

<div class="absolute left-1/3 top-1/2 transform -translate-x-1/2 -translate-y-1/2">
  <p>Push</p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Arrow_right.svg/2560px-Arrow_right.svg.png" alt="Push" class="w-32">
</div>

---
transition: slide-left
---

# GitHub Workflow

<div class="flex justify-around items-center h-full">
  <div class="flex flex-col items-center">
    <div class="bg-gray-200 p-4 rounded shadow-md">
      <p>Fake Filesystem</p>
      <ul>
        <li>file1.txt</li>
        <li>file2.txt</li>
        <li>directory/</li>
      </ul>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-blue-200 p-4 rounded-full shadow-md">
      <p>Local Git Repo</p>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-green-200 p-4 rounded-full shadow-md">
      <p>Main GitHub Repo</p>
    </div>
  </div>
</div>

<div class="absolute left-2/3 top-1/2 transform -translate-x-1/2 -translate-y-1/2">
  <p>Pull</p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Arrow_right.svg/2560px-Arrow_right.svg.png" alt="Pull" class="w-32 transform rotate-180">
</div>

---
transition: slide-left
---

# GitHub Workflow

<div class="flex justify-around items-center h-full">
  <div class="flex flex-col items-center">
    <div class="bg-gray-200 p-4 rounded shadow-md">
      <p>Fake Filesystem</p>
      <ul>
        <li>file1.txt</li>
        <li>file2.txt</li>
        <li>directory/</li>
      </ul>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-blue-200 p-4 rounded-full shadow-md">
      <p>Local Git Repo</p>
    </div>
  </div>
  <div class="flex flex-col items-center">
    <div class="bg-green-200 p-4 rounded-full shadow-md">
      <p>Main GitHub Repo</p>
    </div>
  </div>
</div>

<div class="absolute left-1/3 top-1/2 transform -translate-x-1/2 -translate-y-1/2">
  <p>Push</p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Arrow_right.svg/2560px-Arrow_right.svg.png" alt="Push" class="w-32">
</div>
<div class="absolute left-2/3 top-1/2 transform -translate-x-1/2 -translate-y-1/2">
  <p>Pull</p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Arrow_right.svg/2560px-Arrow_right.svg.png" alt="Pull" class="w-32 transform rotate-180">
</div>


# **Example**