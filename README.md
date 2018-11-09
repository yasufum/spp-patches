# SPP Patches

## What is this?

This repository is for storing all of patches of SPP.

## Description

SPP is updated by applying a patch created with `git format-patch`
command and sent from a developer via e-mail.

This repository is for storing all of patches created by myself and
sent from developers.

Patches before sending via email are stored in `pre-mailed` directory,
and after mailed patches are in `mailed` directory.

Under the `mailed` and `pre-mailed` directory, patches are grouped for
patch set and the name of directory of patch set consists of date and
arbitrary keywords such as `20181109-add_pri_xxx_cmd`.

### Mailed Patches

To find the status, patches merged to the repository are moved to
`mailed/done` directory.

### Pre-mailed Patches

Similar to mailed patches, it is also move to `pre-mailed/done`
directory if patches are mailed.
