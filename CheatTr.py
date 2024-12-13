import libmem as lib
import os
import sys

def GetProcess():
    return lib.find_process("EE2X.exe")
def GetModuleBase():
    return lib.find_module_ex(GetProcess(), GetProcess().name)
def InfRes_Assemble():
    return lib.assemble("mov [ebx+edi*4+000000A8],(float)999999")

def AOBSCAN_EE2X():
    return lib.sig_scan("D9 84 BB A8 00 00 00", GetModuleBase().base + 0x3EBDC5, GetModuleBase().size)

def WriteMem_InfRes():
    return lib.write_memory_ex(GetProcess(), AOBSCAN_EE2X(), bytearray(InfRes_Assemble()))