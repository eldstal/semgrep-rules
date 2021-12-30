#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <stdarg.h>

int main(int argc, char** argv) {

  // Evil, potentially controlled by an attacker
  char fmt[256];

  char buf[256];
  FILE* f;
  int fd;

  //ok: variable-scanf-fmt
  scanf(                    "This is OK");

  //ok: variable-scanf-fmt
  fscanf(f,                 "This is OK");

  //ok: variable-scanf-fmt
  sscanf(buf,               "This is OK");


  va_list va;

  //ok: variable-scanf-fmt
  vscanf(                    "This is OK", va);

  //ok: variable-scanf-fmt
  vfscanf(f,                 "This is OK", va);

  //ok: variable-scanf-fmt
  vsscanf(buf,               "This is OK", va);


  //ruleid: variable-scanf-fmt
  scanf(                    fmt);

  //ruleid: variable-scanf-fmt
  fscanf(f,                 fmt);

  //ruleid: variable-scanf-fmt
  sscanf(buf,               fmt);

  va_list va;

  //ruleid: variable-scanf-fmt
  vscanf(                    fmt, va);

  //ruleid: variable-scanf-fmt
  vfscanf(f,                 fmt, va);

  //ruleid: variable-scanf-fmt
  vsscanf(buf,               fmt, va);

}
