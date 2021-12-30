#!/usr/bin/env python3

def imported_and_safe(cmd):
  from os import system
  from subprocess import run, call, check_output

  safe = "ls"

  #ok: insecure-os-command
  system("ls")

  #ok: insecure-os-command
  system(safe)

  #ok: insecure-os-command
  run("ls")

  #ok: insecure-os-command
  run(safe)

  #ok: insecure-os-command
  call("ls")

  #ok: insecure-os-command
  call(safe)

  #ok: insecure-os-command
  call(cmd)

  #ok: insecure-os-command
  check_output("ls")

  #ok: insecure-os-command
  check_output(safe)

def namespaced_and_safe(cmd):
  import os
  import subprocess

  safe = "ls"

  #ok: insecure-os-command
  os.system("ls")

  #ok: insecure-os-command
  os.system(safe)

  #ok: insecure-os-command
  subprocess.run("ls")

  #ok: insecure-os-command
  subprocess.run(safe)

  #ok: insecure-os-command
  subprocess.call("ls")

  #ok: insecure-os-command
  subprocess.call(safe)

  #ok: insecure-os-command
  subprocess.check_call(cmd)

  #ok: insecure-os-command
  subprocess.check_call("ls")

  #ok: insecure-os-command
  subprocess.check_call(safe)

  #ok: insecure-os-command
  subprocess.check_output(cmd)

  #ok: insecure-os-command
  subprocess.check_output("ls")

  #ok: insecure-os-command
  subprocess.check_output(safe)


def imported_and_dangerous(cmd):
  from os import system
  from subprocess import run,call,check_output

  #ruleid: insecure-os-command
  system(cmd)

  #ruleid: insecure-os-command
  system("ls " + cmd)

  #ruleid: insecure-os-command
  run(cmd)

  #ruleid: insecure-os-command
  run("ls " + cmd)

  #ruleid: insecure-os-command
  call(cmd, shell=True)

  #ruleid: insecure-os-command
  call("ls " + cmd, shell=True)

  #ruleid: insecure-os-command
  check_output(cmd, shell=True)

  #ruleid: insecure-os-command
  check_output("ls " + cmd, shell=True)



def namespaced_and_dangerous(cmd):
  import os
  import subprocess

  #ruleid: insecure-os-command
  os.system(cmd)

  #ruleid: insecure-os-command
  os.system("ls " + cmd)

  #ruleid: insecure-os-command
  os.system(f"ls {cmd}")

  #ruleid: insecure-os-command
  subprocess.run(cmd)

  #ruleid: insecure-os-command
  subprocess.run("ls " + cmd)

  #ruleid: insecure-os-command
  subprocess.run(f"ls {cmd}")

  #ruleid: insecure-os-command
  subprocess.call(cmd, shell=True)

  #ruleid: insecure-os-command
  subprocess.call("ls " + cmd, shell=True)

  #ruleid: insecure-os-command
  subprocess.call(f"ls {cmd}", shell=True)

  #ruleid: insecure-os-command
  subprocess.check_call("ls " + cmd, shell=True)

  #ruleid: insecure-os-command
  subprocess.check_call(f"ls {cmd}", shell=True)

  #ruleid: insecure-os-command
  subprocess.check_output("ls " + cmd, shell=True)

  #ruleid: insecure-os-command
  subprocess.check_output(f"ls {cmd}", shell=True)

