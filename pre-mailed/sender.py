#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2018 Nippon Telegraph and Telephone Corporation

import argparse
import glob
import os
import subprocess

addresses = {
        'spp': [
            "spp@dpdk.org",
            "ferruh.yigit@intel.com",
            "ogawa.yasufumi@lab.ntt.co.jp"]
        }

CMD = ['git', 'send-email']


def parse_args():
    parser = argparse.ArgumentParser(
        description="Helper tool for git send-email")

    parser.add_argument(
        '-p', '--patch',
        type=str,
        help="Patch or its directory")

    parser.add_argument(
        '--to',
        type=str,
        action='append',
        help="E-mail address, enable multiple emails")

    parser.add_argument(
        '-t', '--target-ml',
        type=str,
        default='spp',
        help="Target ML, default is spp")

    parser.add_argument(
        '--in-reply-to',
        type=str,
        help="Message ID of previous patch mail")

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Print command and do not send email")

    return parser.parse_args()


def error_exit(msg):
    print("Error: {}".format(msg))
    exit()


def main():

    args = parse_args()

    if args.patch is None:
        error_exit("Patch dir with '-p' is required!")

    if args.to is not None:
        addrs = args.to
    else:
        addrs = addresses[args.target_ml]
    for m in addrs:
        CMD.append('--to')
        CMD.append(m)

    # Check patch format, it should include cover letter if it is dir
    if os.path.isdir(args.patch):
        files = glob.glob('{}/*'.format(args.patch))
        if len(files) > 1:
            # Check if cover letter is included
            flg = False
            for f in files:
                f = f.split('/')[-1]

                # Check if v2 or later
                if f.startswith('v'):
                    if args.in_reply_to is None:
                        error_exit(
                                "'--in-reply-to' with message ID is required")
                    # remove ver tag nouse for checking cover letter,
                    # such as 'v2-'
                    f = '-'.join(f.split('-')[1:])

                # Check format of cover letter name
                if f.startswith('0000') and f.endswith('.patch'):
                    flg = True
                    break

            if flg is not True:
                error_exit("No cover letter is included!")

            CMD.append('--annotate')
    else:
        if not args.patch.endswith('.patch'):
            error_exit("invalid patch, not have extension '.patch'")
        else:
            print(args.patch)
    CMD.append(args.patch)

    if args.dry_run is True:
        print(' '.join(CMD))
    else:
        subprocess.call(CMD)


if __name__ == '__main__':
    main()
