
;; Display current column number
(setq column-number-mode t)

;; Backup files in one spot
(setq
   backup-by-copying t
   backup-directory-alist '(("." . "~/.emacs.d/backups"))
   delete-old-versions t
   kept-new-versions 6
   kept-old-versions 2
   version-control t)

;; Theme
(add-to-list 'custom-theme-load-path "~/.emacs.d/themes/")
(load-theme 'zenburn t)
