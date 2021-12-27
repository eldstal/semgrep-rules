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

  //ok: variable-printf-fmt
  printf(                    "This is OK");

  //ok: variable-printf-fmt
  fprintf(f,                 "This is OK");

  //ok: variable-printf-fmt
  dprintf(fd,                "This is OK");

  //ok: variable-printf-fmt
  sprintf(buf,               "This is OK");

  //ok: variable-printf-fmt
  snprintf(buf, sizeof(buf), "This is OK");

  va_list va;

  //ok: variable-printf-fmt
  vprintf(                    "This is OK", va);

  //ok: variable-printf-fmt
  vfprintf(f,                 "This is OK", va);

  //ok: variable-printf-fmt
  vdprintf(fd,                "This is OK", va);

  //ok: variable-printf-fmt
  vsprintf(buf,               "This is OK", va);

  //ok: variable-printf-fmt
  vsnprintf(buf, sizeof(buf), "This is OK", va);


  //ruleid: variable-printf-fmt
  printf(                    fmt);

  //ruleid: variable-printf-fmt
  fprintf(f,                 fmt);

  //ruleid: variable-printf-fmt
  dprintf(fd,                fmt);

  //ruleid: variable-printf-fmt
  sprintf(buf,               fmt);

  //ruleid: variable-printf-fmt
  snprintf(buf, sizeof(buf), fmt);

  va_list va;

  //ruleid: variable-printf-fmt
  vprintf(                    fmt, va);

  //ruleid: variable-printf-fmt
  vfprintf(f,                 fmt, va);

  //ruleid: variable-printf-fmt
  vdprintf(fd,                fmt, va);

  //ruleid: variable-printf-fmt
  vsprintf(buf,               fmt, va);

  //ruleid: variable-printf-fmt
  vsnprintf(buf, sizeof(buf), fmt, va);

}
