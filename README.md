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

### 1. Mailed Patches

To find the status, patches merged to the repository are moved to
`mailed/done` directory.

### 2. Pre-mailed Patches

Similar to mailed patches, it is also move to `pre-mailed/done`
directory if patches are mailed.

You might failed to send patches by rejecting it from mail server for
security. In this case, you need to install cpan module `Net::SSL`.

```sh
$ cpanm install Net::SSL

# or helper script for doing the same
$ sh cpanm.sh
```

### 3. Helper Tools

Like other OSS projects, sending patches should be done complying with
the rules in SPP. `sender.py` is a helper tool for doing
`git send-email` command more simply.
By using this tool, you do not need to input emails of the SPP ML and
maintainers everytime.

#### How to use sender.py

##### (1) Send patches at first time

Without sending v2 or later versions, you simply specify patch's
directory. This command runs `git send-email` with emails of SPP.

```sh
$ python3 sender.py -p PATCH_DIR
```

You can check if your command generated from `sender.py` is correct
by using `--dry-run` option. It does not run `git send-email` itself.

```sh
$ python3 sender.py -p PATCH_DIR --dry-run
git send-email --to spp@dpdk.org --to ... PATCH_DIR
```

##### (2) Send patches v2 or later

Run `sender.py` with message ID as similar as `git send-email`
if you send v2 or later version.
This script checks if message ID is given, and terminates command
if no message ID given for v2 or later.

```sh
$ python3 sender.py --in-reply-with MESSAGE_ID -p PATCH_DIR
```

##### (3) Test by sending to your private email address

You can test this script works correctly by sending patches to your
private address before sending SPP ML.
If you give address with `--to` option, It replaces the addresses of
SPP. You can also give several addresses.

```sh
$ python3 sender.py --to addr1@exp.com --to addr2@exp.com -p PATCH_DIR
```

All of options are referred with help.
```sh
$ python3 sender.py -h
```
