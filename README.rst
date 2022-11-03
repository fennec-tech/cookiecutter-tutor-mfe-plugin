Tutor MFE Plugin Cookiecutter 🍪
================================

This is a (WIP) `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/tutorial2.html>`__ which creates a `Tutor plugin <https://docs.tutor.overhang.io/plugins.html>`__ with the minimal code needed to add an Open edX micro-frontend.

Features
--------
- Adds a new MFE with basic configuration.
- Disable existing MFE configuration.
- Add a `tutor images build <mfe-name>` entry to build the MFE's dev image separately.

Roadmap
#######
- Populate some configuration patches for services on which an MFE depends.
- Add a `tutor init` job to toggle any required waffle flags/switches.

Usage
-----
A. With Tutor using the Scaffold plugin
#######################################

1. Install `Tutor <https://docs.tutor.overhang.io/>`__
   .. code-block: bash
      pip install tutor
2. Install and enable the `Scaffold plugin <https://github.com/fennec-tech/tutor-contrib-scaffold>`__:
   .. code-block: bash
      pip install git+https://github.com/fennec-tech/tutor-contrib-scaffold
3. Use the cookiecutter:
   .. code-block: bash
      tutor scaffold tutor-mfe-plugin

B. With `cookiecutter`
######################
1. Install ``cookiecutter`` package:
   .. code-block: bash
      pip install cookiecutter
2. Use the cookiecutter:
   .. code-block: bash
      cookiecutter https://github.com/fennec-tech/cookiecutter-tutor-mfe-plugin.git

The generated plugin
####################
Please keep the "contrib" part in your generated package name to differentiate it from official tutor plugins.

Once you have generated your plugin, you can start using it right away (even if you would still need to tweak the configuration or add patches)
   .. code-block: bash

      pip install -e ./tutor-contrib-mfe-mymfe
      tutor plugins list # your plugin should appear here
      tutor plugins enable mfe-mymfe # hack at it!

Troubleshooting
---------------
This Tutor plugin template is maintained by `Abderraouf Mehdi Bouhali <https://github.com/ARMBouhali>`__ from `Fennec Technologies <https://fennectech.com>`__ (`@fennec-tech <https://github.com/ARMBouhali>`__). Community support is available from the official `Open edX forum <https://discuss.openedx.org>`_.
Do you need help using this template? See the `troubleshooting <https://docs.tutor.overhang.io/troubleshooting.html>`_ section from the Tutor documentation.

Contributing
------------
This project is a work in progress, as it depends on the `tutor-mfe plugin <https://github.com/overhangio/tutor-mfe>`__ which is evolving to accommodate the increasing number of adopted Open edX MFEs.
Any contributions, suggestions, feature requests or bug reports are welcome on GitHub `issues <https://github.com/fennec-tech/cookiecutter-tutor-mfe-plugin/issues>`__ and `pull requests <https://github.com/fennec-tech/cookiecutter-tutor-mfe-plugin>`__, as well as on the official Open edX `forum <https://discuss.openedx.org>`__ and `Slack group <https://openedx-slack-invite.herokuapp.com>`__.

License
-------
This software is a derivated work of `cookiecutter-tutor-plugin <https://github.com/overhangio/cookiecutter-tutor-plugin>`__, <licensed under the terms of the `AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`__. 