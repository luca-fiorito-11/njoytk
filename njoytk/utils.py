# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:16:18 2018

@author: Fiorito_L
"""

__author__ = "Luca Fiorito"

import os
import argparse
import subprocess as sp

def run_process(cmd, cwd=None, timeout=36000, verbose=True):
    """Run process from shell
    """
    process = sp.Popen("exec " + cmd,
                       shell=True,
                       cwd=cwd,
                       stdin=None,
                       stdout=sp.PIPE,
                       stderr=sp.PIPE,)
    try:
        stdoutdata, stderrdata = process.communicate(timeout=timeout)
    except sp.TimeoutExpired as exc:
        process.kill()
        stdoutdata, stderrdata = process.communicate()
        stderrdata += (r"'{}' took longer than {} seconds to complete and it was killed".format(cmd, timeout)).encode()
    stdout = stdoutdata.decode('utf-8', errors='ignore').rstrip()
    stderr = stderrdata.decode('utf-8', errors='ignore').rstrip()
    if verbose: print(stdout)
    if process.returncode: print(stderr)
    return process.returncode, stdout, stderr

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def is_valid_file(parser, arg, r=True, w=False, x=False):
    arg = os.path.abspath(os.path.realpath(os.path.normpath(arg)))
    if not os.path.isfile(arg):
        parser.error("File {} does not exist".format(arg))
    if r and not os.access(arg, os.R_OK):
        parser.error("File {} is not readable".format(arg))
    if w and not os.access(arg, os.W_OK):
        parser.error("File {} is not writable".format(arg))
    if x and not os.access(arg, os.X_OK):
        parser.error("File {} is not executable".format(arg))
    return arg


def is_valid_dir(parser, arg, mkdir=False):
    arg = os.path.abspath(os.path.realpath(os.path.normpath(arg)))
    if os.path.isdir(arg):
        return arg
    if mkdir:
        os.makedirs(arg, exist_ok=True)
    else:
        parser.error("Directory {} does not exist".format(arg))
    return arg

def which(program):
    """Mimic the behavior of the UNIX 'which' command.
    """
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None

def force_symlink(file1, file2):
    """Mimic the behavior of the UNIX 'ln -sf' command.
    """
    file1 = os.path.abspath(os.path.normpath(file1))
    try:
        os.symlink(file1, file2)
    except FileExistsError:
        os.remove(file2)
        os.symlink(file1, file2)
