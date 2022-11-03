from glob import glob
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__

########################################
# CONFIGURATION
########################################

mfe_config = {
    "name": "{{ cookiecutter.mfe_app_name }}",
    "port": {{ cookiecutter.mfe_app_port }},
    "repository": "{{ cookiecutter.mfe_app_repository }}",
    {%- if cookiecutter.mfe_app_version %}
    "version": "{{ cookiecutter.existing_mfe_app_config }}",
    {%- endif %}
}

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        ("{{ cookiecutter.mfe_official_name|upper|replace('-', '_') }}_VERSION", __version__),
        {%- if not cookiecutter.existing_config_to_override %}
        # Add new {{ cookiecutter.mfe_app_name }} MFE configuration
        ("{{ cookiecutter.mfe_official_name|upper|replace('-', '_') }}_MFE_APP", mfe_config),
        {%- endif %}
    ]
)


{%- if cookiecutter.existing_config_to_override %}
hooks.Filters.CONFIG_OVERRIDES.add_items(
    [
        # Override existing {{ cookiecutter.mfe_app_name }} MFE configuration
        ("{{ cookiecutter.existing_config_to_override }}", mfe_config),
    ]
)
{%- endif %}

########################################
# INITIALIZATION TASKS
########################################

# To run the script from templates/{{ cookiecutter.mfe_official_name }}/tasks/myservice/init, add:
# hooks.Filters.COMMANDS_INIT.add_item((
#     "myservice",
#     ("{{ cookiecutter.mfe_official_name }}", "tasks", "myservice", "init"),
# ))


########################################
# DOCKER IMAGE MANAGEMENT
########################################

# To build an image with `tutor images build {{ cookiecutter.mfe_app_name }}
# using tutor-mfe's build context located at <tutor-root>/env/plugins/mfe/build/mfe
hooks.Filters.IMAGES_BUILD.add_item((
    "{{ cookiecutter.mfe_app_name }}",
    ("plugins", "mfe", "build", "mfe"),
    "docker.io/{{ cookiecutter.mfe_app_name }}:latest",
    ("--target", "{{ cookiecutter.mfe_app_name }}-dev"),
))
# To pull/push an image with `tutor images pull myimage` and `tutor images push myimage`, write:
hooks.Filters.IMAGES_PULL.add_item((
    "{{ cookiecutter.mfe_app_name }}",
    "docker.io/{{ cookiecutter.mfe_app_name }}:latest",
))
hooks.Filters.IMAGES_PUSH.add_item((
    "{{ cookiecutter.mfe_app_name }}",
    "docker.io/{{ cookiecutter.mfe_app_name }}:latest",
))


########################################
# PATCH LOADING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

# For each file in {{ cookiecutter.module_name }}/patches,
# apply a patch based on the file's name and contents.
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("{{ cookiecutter.module_name }}", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
