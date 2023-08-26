# Files in the config/locales directory are used for internationalization
# and are automatically loaded by Rails. If you want to use locales other
# than English, add the necessary files in this directory.
#
# To use the locales, use `I18n.t`:
#
#     I18n.t 'hello'
#
# In views, this is aliased to just `t`:
#
#     <%= t('hello') %>
#
# To use a different locale, set it with `I18n.locale`:
#
#     I18n.locale = :es
#
# This would use the information in config/locales/es.yml.
#
# To learn more, please read the Rails Internationalization guide
# available at http://guides.rubyonrails.org/i18n.html.

en:
  wizard:
    next: "Next"
    back: "Back"
    build: "Build"
    start: "Start"
    "yes": "Yes"
    "no": "No"
    new-build: "New build"
    show:
      preparing-build: "Preparing build..."
      building-image: "Building coreboot image..."
      waiting-for-build-server: "Waiting for Build server to take action..."
      build-succeeded: "Build succeeded!"
      build-succeeded-extra: "Your build was successful. Please ensure, that you decrypt the image with your private key before flashing"
      download: "Download"
      build-failed: "Build failed"
      build-failed-extra: ""
      build-unconfigured: "Build still needs to be configured"
    disclaimer:
      title: "DISCLAIMER"
      rom-upload-content: |
        The backup of your BIOS chip contains various binary components that we
        are not allowed to redistribute. Therefore, we will extract them from
        your backup and place them into the new image along with coreboot. The
        new image will be encrypted for you only, to circumvent copyright issues.
    select-bios-file: "Select BIOS File"
    gpg-key: "Your GPG public key"
    email-address: "Type in your email address"
    choose-vendor: "Choose the vendor of your device"
    choose-device: "Choose the model of your device"
  options:
    enums:
      select-payload: "Please select a payload which should be loaded after coreboot finished"
    booleans:
      seabios: "SeaBIOS"
      grub2: "GRUB2"
      deactivate-tpm: "Deactivate TPM"
      bootchart: "Create boot process timestamps"
    arrays:
      lock-firmware: "Lock coreboot firmware against flash writes and reads"
  mailer:
    build_mailer:
      build_started_mail:
        subject: Your build has started
        content: |
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

          %{link}
      build_done_success_mail:
        subject: Your build has succeeded
        content: |
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

          %{link}
      build_done_fail_mail:
        subject: Your build has failed
        content: |
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
