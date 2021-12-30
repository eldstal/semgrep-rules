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

  //ok: blender-fmt-wrappers
  _RNA_warning("This is OK");

  //ok: blender-fmt-wrappers
  exr_printf("This is OK");

  //ok: blender-fmt-wrappers
  deg_debug_fprintf(NULL,"This is OK");

  //ok: blender-fmt-wrappers
  WM_reportf(NULL,"This is OK");

  //ok: blender-fmt-wrappers
  BKE_gpencil_modifier_set_error(NULL,"This is OK");

  //ok: blender-fmt-wrappers
  BLI_dynstr_appendf(NULL,"This is OK");

  //ok: blender-fmt-wrappers
  BKE_gpencil_modifier_set_error(NULL,"This is OK");

  //ok: blender-fmt-wrappers
  BLO_reportf_wrap(NULL,NULL,"This is OK");

  //ok: blender-fmt-wrappers
  BKE_modifier_set_error(NULL,NULL,"This is OK");

  //ok: blender-fmt-wrappers
  BKE_reportf(NULL,NULL,"This is OK");


  //ruleid: blender-fmt-wrappers
  _RNA_warning(fmt);

  //ruleid: blender-fmt-wrappers
  exr_printf(fmt);

  //ruleid: blender-fmt-wrappers
  deg_debug_fprintf(NULL,fmt);

  //ruleid: blender-fmt-wrappers
  WM_reportf(NULL,fmt);

  //ruleid: blender-fmt-wrappers
  BKE_gpencil_modifier_set_error(NULL,fmt);

  //ruleid: blender-fmt-wrappers
  BLI_dynstr_appendf(NULL,fmt);

  //ruleid: blender-fmt-wrappers
  BKE_gpencil_modifier_set_error(NULL,fmt);

  //ruleid: blender-fmt-wrappers
  BLO_reportf_wrap(NULL,NULL,fmt);

  //ruleid: blender-fmt-wrappers
  BKE_modifier_set_error(NULL,NULL,fmt);

  //ruleid: blender-fmt-wrappers
  BKE_reportf(NULL,NULL,fmt);
}
