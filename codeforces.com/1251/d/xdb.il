// (wrapper runtime-invoke) <Module>:runtime_invoke_void__this___object (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0043
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.1   
IL_002c: ldind.ref 
IL_002d: ldarg.3   
IL_002e: calli     <object>
IL_0033: leave     IL_0041
IL_0038: stloc.1   
IL_0039: ldarg.2   
IL_003a: ldloc.1   
IL_003b: stind.ref 
IL_003c: leave     IL_0041
IL_0041: ldloc.0   
IL_0042: ret       
IL_0043: mono_ldptr_int_req_flag
IL_0045: ldind.u4  
IL_0046: brfalse   IL_0067
IL_004b: mono_not_taken
IL_004d: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0053: dup       
IL_0054: brfalse   IL_0066
IL_0059: dup       
IL_005a: mono_objaddr
IL_005c: ldc.i4    136
IL_0061: add       
IL_0062: ldc.i4.1  
IL_0063: stind.i4  
IL_0064: mono_rethrow
IL_0066: pop       
IL_0067: ldarg.0   
IL_0068: ldarg.1   
IL_0069: ldind.ref 
IL_006a: ldarg.3   
IL_006b: calli     <object>
IL_0070: ldloc.0   
IL_0071: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// (wrapper alloc) object:AllocSmall (intptr,intptr)
IL_0000: mono_tls  3
IL_0006: stloc.0   
IL_0007: ldarg.1   
IL_0008: stloc.1   
IL_0009: ldloc.0   
IL_000a: ldc.i4    1192
IL_000f: add       
IL_0010: ldc.i4.1  
IL_0011: mono_atomic_store_i40
IL_0017: ldloc.1   
IL_0018: ldc.i4.7  
IL_0019: add       
IL_001a: ldc.i4.s  -8
IL_001c: and       
IL_001d: stloc.1   
IL_001e: ldloc.0   
IL_001f: ldc.i4    1640
IL_0024: add       
IL_0025: stloc.2   
IL_0026: ldloc.2   
IL_0027: ldind.i   
IL_0028: stloc.3   
IL_0029: ldloc.3   
IL_002a: ldloc.1   
IL_002b: conv.i    
IL_002c: add       
IL_002d: stloc.s   4
IL_002f: ldloc.s   4
IL_0031: ldloc.0   
IL_0032: ldc.i4    1648
IL_0037: add       
IL_0038: ldind.i   
IL_0039: blt.un.s  IL_0060
IL_003b: mono_not_taken
IL_003d: ldloc.0   
IL_003e: ldc.i4    1192
IL_0043: add       
IL_0044: ldc.i4.0  
IL_0045: mono_atomic_store_i40
IL_004b: ldarg.0   
IL_004c: ldloc.1   
IL_004d: mono_icall <mono_gc_alloc_obj>
IL_0053: dup       
IL_0054: brtrue    IL_005f
IL_0059: newobj    <System.OutOfMemoryException:.ctor ()>
IL_005e: throw     
IL_005f: ret       
IL_0060: ldloc.2   
IL_0061: ldloc.s   4
IL_0063: stind.i   
IL_0064: ldloc.3   
IL_0065: ldarg.0   
IL_0066: stind.i   
IL_0067: ldloc.0   
IL_0068: ldc.i4    1192
IL_006d: add       
IL_006e: ldc.i4.0  
IL_006f: mono_atomic_store_i42
IL_0075: ldloc.3   
IL_0076: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// (wrapper managed-to-native) object:__icall_wrapper_mono_generic_class_init (intptr)
IL_0000: ldarg.0   
IL_0001: mono_jit_icall_addr2
IL_0007: calli     <intptr>
IL_000c: mono_ldptr_int_req_flag
IL_000e: ldind.u4  
IL_000f: brfalse   IL_0030
IL_0014: mono_not_taken
IL_0016: mono_icall <mono_thread_interruption_checkpoint>
IL_001c: dup       
IL_001d: brfalse   IL_002f
IL_0022: dup       
IL_0023: mono_objaddr
IL_0025: ldc.i4    136
IL_002a: add       
IL_002b: ldc.i4.1  
IL_002c: stind.i4  
IL_002d: mono_rethrow
IL_002f: pop       
IL_0030: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// (wrapper alloc) object:AllocVector (intptr,intptr)
IL_0000: mono_tls  3
IL_0006: stloc.0   
IL_0007: ldarg.1   
IL_0008: ldc.i4    2147483647
IL_000d: conv.u    
IL_000e: ble.un.s  IL_0022
IL_0010: mono_not_taken
IL_0012: ldarg.1   
IL_0013: ldc.i4.0  
IL_0014: blt.s     IL_001c
IL_0016: newobj    <System.OutOfMemoryException:.ctor ()>
IL_001b: throw     
IL_001c: newobj    <System.OverflowException:.ctor ()>
IL_0021: throw     
IL_0022: ldarg.0   
IL_0023: ldc.i4.0  
IL_0024: add       
IL_0025: ldind.i   
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldind.u4  
IL_002d: conv.i    
IL_002e: ldarg.1   
IL_002f: mul.ovf.un
IL_0030: ldc.i4.s  32
IL_0032: add.ovf.un
IL_0033: stloc.1   
IL_0034: leave     IL_0040
IL_0039: pop       
IL_003a: newobj    <System.OutOfMemoryException:.ctor ()>
IL_003f: throw     
IL_0040: ldloc.0   
IL_0041: ldc.i4    1192
IL_0046: add       
IL_0047: ldc.i4.1  
IL_0048: mono_atomic_store_i40
IL_004e: ldloc.1   
IL_004f: ldc.i4.7  
IL_0050: add       
IL_0051: ldc.i4.s  -8
IL_0053: and       
IL_0054: stloc.1   
IL_0055: ldloc.1   
IL_0056: ldc.i4    8000
IL_005b: bgt.un.s  IL_007a
IL_005d: ldloc.0   
IL_005e: ldc.i4    1640
IL_0063: add       
IL_0064: stloc.2   
IL_0065: ldloc.2   
IL_0066: ldind.i   
IL_0067: stloc.3   
IL_0068: ldloc.3   
IL_0069: ldloc.1   
IL_006a: conv.i    
IL_006b: add       
IL_006c: stloc.s   4
IL_006e: ldloc.s   4
IL_0070: ldloc.0   
IL_0071: ldc.i4    1648
IL_0076: add       
IL_0077: ldind.i   
IL_0078: blt.un.s  IL_00a0
IL_007a: mono_not_taken
IL_007c: ldloc.0   
IL_007d: ldc.i4    1192
IL_0082: add       
IL_0083: ldc.i4.0  
IL_0084: mono_atomic_store_i40
IL_008a: ldarg.0   
IL_008b: ldloc.1   
IL_008c: ldarg.1   
IL_008d: mono_icall <mono_gc_alloc_vector>
IL_0093: dup       
IL_0094: brtrue    IL_009f
IL_0099: newobj    <System.OutOfMemoryException:.ctor ()>
IL_009e: throw     
IL_009f: ret       
IL_00a0: ldloc.2   
IL_00a1: ldloc.s   4
IL_00a3: stind.i   
IL_00a4: ldloc.3   
IL_00a5: ldarg.0   
IL_00a6: stind.i   
IL_00a7: ldloc.3   
IL_00a8: mono_objaddr
IL_00aa: ldc.i4.s  24
IL_00ac: add       
IL_00ad: ldarg.1   
IL_00ae: stind.i4  
IL_00af: ldloc.0   
IL_00b0: ldc.i4    1192
IL_00b5: add       
IL_00b6: ldc.i4.0  
IL_00b7: mono_atomic_store_i42
IL_00bd: ldloc.3   
IL_00be: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// System.Diagnostics.DiagnosticsConfiguration:.cctor ()
IL_0000: ret       
// System.Diagnostics.ConfigurationManagerInternalFactory/Instance:.cctor ()
IL_0000: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// (wrapper managed-to-native) System.Reflection.Assembly:GetEntryAssembly ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.Environment:GetMachineConfigPath ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.AppDomain:getCurDomain ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper remoting-invoke-with-check) System.AppDomain:get_SetupInformation ()
IL_0000: ldarg.0   
IL_0001: ldarg.0   
IL_0002: mono_objaddr
IL_0004: ldind.i   
IL_0005: ldc.i4.0  
IL_0006: add       
IL_0007: ldind.i   
IL_0008: mono_classconst <TransparentProxy>
IL_000e: bne.un    IL_0032
IL_0013: ldarg.0   
IL_0014: mono_objaddr
IL_0016: ldc.i4.s  16
IL_0018: add       
IL_0019: ldind.ref 
IL_001a: mono_objaddr
IL_001c: ldc.i4.s  40
IL_001e: add       
IL_001f: ldind.i4  
IL_0020: ldc.i4.m1 
IL_0021: beq       IL_002c
IL_0026: call      <(wrapper xdomain-invoke) System.AppDomain:get_SetupInformation ()>
IL_002b: ret       
IL_002c: call      <(wrapper remoting-invoke) System.AppDomain:get_SetupInformation ()>
IL_0031: ret       
IL_0032: call      <System.AppDomain:get_SetupInformation ()>
IL_0037: ret       
// (wrapper managed-to-native) System.AppDomain:getSetup (System.AppDomain)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldloca.s  0
IL_0010: mono_ldptr3
IL_0016: calli     <AppDomain&,RuntimeStructs/MonoError&>
IL_001b: mono_ldptr_int_req_flag
IL_001d: ldind.u4  
IL_001e: brfalse   IL_003f
IL_0023: mono_not_taken
IL_0025: mono_icall <mono_thread_interruption_checkpoint>
IL_002b: dup       
IL_002c: brfalse   IL_003e
IL_0031: dup       
IL_0032: mono_objaddr
IL_0034: ldc.i4    136
IL_0039: add       
IL_003a: ldc.i4.1  
IL_003b: stind.i4  
IL_003c: mono_rethrow
IL_003e: pop       
IL_003f: ret       
// (wrapper managed-to-native) System.IO.MonoIO:get_VolumeSeparatorChar ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper managed-to-native) Mono.SafeStringMarshal:StringToUtf8 (string)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <string&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.Environment:internalGetEnvironmentVariable_native (intptr)
IL_0000: ldarg.0   
IL_0001: ldloca.s  0
IL_0003: mono_ldptr2
IL_0009: calli     <intptr,RuntimeStructs/MonoError&>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) Mono.SafeStringMarshal:GFree (intptr)
IL_0000: ldarg.0   
IL_0001: ldloca.s  0
IL_0003: mono_ldptr2
IL_0009: calli     <intptr,RuntimeStructs/MonoError&>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) System.IO.MonoIO:get_DirectorySeparatorChar ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper managed-to-native) System.IO.MonoIO:get_AltDirectorySeparatorChar ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper managed-to-native) System.IO.MonoIO:get_PathSeparator ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper managed-to-native) System.Environment:get_Platform ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// (wrapper managed-to-native) System.Buffer:InternalMemcpy (byte*,byte*,int)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: mono_ldptr2
IL_0009: calli     <byte*,byte*,int>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) string:FastAllocateString (int)
IL_0000: ldarg.0   
IL_0001: ldloca.s  0
IL_0003: mono_ldptr2
IL_0009: calli     <int,RuntimeStructs/MonoError&>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper stelemref) object:virt_stelemref_object (intptr,object)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldelema   <Object>
IL_0007: ldarg.2   
IL_0008: stind.ref 
IL_0009: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:IsGenericVariable (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:HasInstantiation (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:IsArray (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:IsByRef (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:IsPointer (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper stelemref) object:virt_stelemref_sealed_class (intptr,object)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldelema   <Object>
IL_0007: stloc.2   
IL_0008: ldarg.2   
IL_0009: brfalse   IL_0028
IL_000e: ldarg.0   
IL_000f: mono_objaddr
IL_0011: ldind.i   
IL_0012: mono_objaddr
IL_0014: ldind.i   
IL_0015: mono_objaddr
IL_0017: ldind.i   
IL_0018: stloc.0   
IL_0019: ldarg.2   
IL_001a: mono_objaddr
IL_001c: ldind.i   
IL_001d: mono_objaddr
IL_001f: ldind.i   
IL_0020: stloc.1   
IL_0021: ldloc.0   
IL_0022: ldloc.1   
IL_0023: bne.un    IL_002c
IL_0028: ldloc.2   
IL_0029: ldarg.2   
IL_002a: stind.ref 
IL_002b: ret       
IL_002c: newobj    <System.ArrayTypeMismatchException:.ctor ()>
IL_0031: throw     
// (wrapper stelemref) object:virt_stelemref_class_small_idepth (intptr,object)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldelema   <Object>
IL_0007: stloc.2   
IL_0008: ldarg.2   
IL_0009: brfalse   IL_003c
IL_000e: ldarg.0   
IL_000f: mono_objaddr
IL_0011: ldind.i   
IL_0012: mono_objaddr
IL_0014: ldind.i   
IL_0015: mono_objaddr
IL_0017: ldind.i   
IL_0018: stloc.0   
IL_0019: ldarg.2   
IL_001a: mono_objaddr
IL_001c: ldind.i   
IL_001d: mono_objaddr
IL_001f: ldind.i   
IL_0020: stloc.1   
IL_0021: ldloc.1   
IL_0022: mono_objaddr
IL_0024: ldc.i4.s  16
IL_0026: add       
IL_0027: ldind.i   
IL_0028: ldloc.0   
IL_0029: mono_objaddr
IL_002b: ldc.i4.s  24
IL_002d: add       
IL_002e: ldind.u2  
IL_002f: ldc.i4.1  
IL_0030: sub       
IL_0031: ldc.i4.s  8
IL_0033: mul       
IL_0034: add       
IL_0035: ldind.i   
IL_0036: ldloc.0   
IL_0037: bne.un    IL_0040
IL_003c: ldloc.2   
IL_003d: ldarg.2   
IL_003e: stind.ref 
IL_003f: ret       
IL_0040: newobj    <System.ArrayTypeMismatchException:.ctor ()>
IL_0045: throw     
// (wrapper remoting-invoke-with-check) object:MemberwiseClone ()
IL_0000: ldarg.0   
IL_0001: ldarg.0   
IL_0002: mono_objaddr
IL_0004: ldind.i   
IL_0005: ldc.i4.0  
IL_0006: add       
IL_0007: ldind.i   
IL_0008: mono_classconst <TransparentProxy>
IL_000e: bne.un    IL_0032
IL_0013: ldarg.0   
IL_0014: mono_objaddr
IL_0016: ldc.i4.s  16
IL_0018: add       
IL_0019: ldind.ref 
IL_001a: mono_objaddr
IL_001c: ldc.i4.s  40
IL_001e: add       
IL_001f: ldind.i4  
IL_0020: ldc.i4.m1 
IL_0021: beq       IL_002c
IL_0026: call      <(wrapper xdomain-invoke) object:MemberwiseClone ()>
IL_002b: ret       
IL_002c: call      <(wrapper remoting-invoke) object:MemberwiseClone ()>
IL_0031: ret       
IL_0032: call      <object:MemberwiseClone ()>
IL_0037: ret       
// (wrapper managed-to-native) object:MemberwiseClone (object)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldloca.s  0
IL_0010: mono_ldptr3
IL_0016: calli     <object&,RuntimeStructs/MonoError&>
IL_001b: mono_ldptr_int_req_flag
IL_001d: ldind.u4  
IL_001e: brfalse   IL_003f
IL_0023: mono_not_taken
IL_0025: mono_icall <mono_thread_interruption_checkpoint>
IL_002b: dup       
IL_002c: brfalse   IL_003e
IL_0031: dup       
IL_0032: mono_objaddr
IL_0034: ldc.i4    136
IL_0039: add       
IL_003a: ldc.i4.1  
IL_003b: stind.i4  
IL_003c: mono_rethrow
IL_003e: pop       
IL_003f: ret       
// (wrapper managed-to-native) System.RuntimeType:GetConstructors_native (System.RuntimeType,System.Reflection.BindingFlags)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldloca.s  0
IL_0011: mono_ldptr3
IL_0017: calli     <RuntimeType&,BindingFlags,RuntimeStructs/MonoError&>
IL_001c: mono_ldptr_int_req_flag
IL_001e: ldind.u4  
IL_001f: brfalse   IL_0040
IL_0024: mono_not_taken
IL_0026: mono_icall <mono_thread_interruption_checkpoint>
IL_002c: dup       
IL_002d: brfalse   IL_003f
IL_0032: dup       
IL_0033: mono_objaddr
IL_0035: ldc.i4    136
IL_003a: add       
IL_003b: ldc.i4.1  
IL_003c: stind.i4  
IL_003d: mono_rethrow
IL_003f: pop       
IL_0040: ret       
// (wrapper managed-to-native) System.Reflection.RuntimeMethodInfo:GetMethodFromHandleInternalType_native (intptr,intptr,bool)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldloca.s  0
IL_0005: mono_ldptr2
IL_000b: calli     <intptr,intptr,bool,RuntimeStructs/MonoError&>
IL_0010: mono_ldptr_int_req_flag
IL_0012: ldind.u4  
IL_0013: brfalse   IL_0034
IL_0018: mono_not_taken
IL_001a: mono_icall <mono_thread_interruption_checkpoint>
IL_0020: dup       
IL_0021: brfalse   IL_0033
IL_0026: dup       
IL_0027: mono_objaddr
IL_0029: ldc.i4    136
IL_002e: add       
IL_002f: ldc.i4.1  
IL_0030: stind.i4  
IL_0031: mono_rethrow
IL_0033: pop       
IL_0034: ret       
// (wrapper managed-to-native) Mono.RuntimeGPtrArrayHandle:GPtrArrayFree (Mono.RuntimeStructs/GPtrArray*)
IL_0000: ldarg.0   
IL_0001: ldloca.s  0
IL_0003: mono_ldptr2
IL_0009: calli     <RuntimeStructs/GPtrArray*,RuntimeStructs/MonoError&>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) System.Reflection.MonoMethodInfo:get_parameter_info (intptr,System.Reflection.MemberInfo)
IL_0000: ldarg.0   
IL_0001: ldarga.s  1
IL_0003: ldloca.s  0
IL_0005: mono_ldptr2
IL_000b: calli     <intptr,MemberInfo&,RuntimeStructs/MonoError&>
IL_0010: mono_ldptr_int_req_flag
IL_0012: ldind.u4  
IL_0013: brfalse   IL_0034
IL_0018: mono_not_taken
IL_001a: mono_icall <mono_thread_interruption_checkpoint>
IL_0020: dup       
IL_0021: brfalse   IL_0033
IL_0026: dup       
IL_0027: mono_objaddr
IL_0029: ldc.i4    136
IL_002e: add       
IL_002f: ldc.i4.1  
IL_0030: stind.i4  
IL_0031: mono_rethrow
IL_0033: pop       
IL_0034: ret       
// (wrapper managed-to-native) System.Reflection.MonoMethodInfo:get_method_attributes (intptr)
IL_0000: ldarg.0   
IL_0001: mono_ldptr2
IL_0007: calli     <intptr>
IL_000c: mono_ldptr_int_req_flag
IL_000e: ldind.u4  
IL_000f: brfalse   IL_0030
IL_0014: mono_not_taken
IL_0016: mono_icall <mono_thread_interruption_checkpoint>
IL_001c: dup       
IL_001d: brfalse   IL_002f
IL_0022: dup       
IL_0023: mono_objaddr
IL_0025: ldc.i4    136
IL_002a: add       
IL_002b: ldc.i4.1  
IL_002c: stind.i4  
IL_002d: mono_rethrow
IL_002f: pop       
IL_0030: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:GetAttributes (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.Reflection.RuntimeConstructorInfo:InternalInvoke (System.Reflection.RuntimeConstructorInfo,object,object[],System.Exception&)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarg.0   
IL_000d: ldarg.1   
IL_000e: ldarg.2   
IL_000f: ldarg.3   
IL_0010: mono_ldptr3
IL_0016: calli     <RuntimeConstructorInfo,object,object[],Exception&>
IL_001b: mono_ldptr_int_req_flag
IL_001d: ldind.u4  
IL_001e: brfalse   IL_003f
IL_0023: mono_not_taken
IL_0025: mono_icall <mono_thread_interruption_checkpoint>
IL_002b: dup       
IL_002c: brfalse   IL_003e
IL_0031: dup       
IL_0032: mono_objaddr
IL_0034: ldc.i4    136
IL_0039: add       
IL_003a: ldc.i4.1  
IL_003b: stind.i4  
IL_003c: mono_rethrow
IL_003e: pop       
IL_003f: ret       
// System.Configuration.ExeConfigurationHost:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.InternalConfigurationHost:.ctor ()>
IL_0006: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void__this__ (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0041
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.3   
IL_002c: calli     <>
IL_0031: leave     IL_003f
IL_0036: stloc.1   
IL_0037: ldarg.2   
IL_0038: ldloc.1   
IL_0039: stind.ref 
IL_003a: leave     IL_003f
IL_003f: ldloc.0   
IL_0040: ret       
IL_0041: mono_ldptr_int_req_flag
IL_0043: ldind.u4  
IL_0044: brfalse   IL_0065
IL_0049: mono_not_taken
IL_004b: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0051: dup       
IL_0052: brfalse   IL_0064
IL_0057: dup       
IL_0058: mono_objaddr
IL_005a: ldc.i4    136
IL_005f: add       
IL_0060: ldc.i4.1  
IL_0061: stind.i4  
IL_0062: mono_rethrow
IL_0064: pop       
IL_0065: ldarg.0   
IL_0066: ldarg.3   
IL_0067: calli     <>
IL_006c: ldloc.0   
IL_006d: ret       
// (wrapper managed-to-native) System.Threading.Monitor:Exit (object)
IL_0000: ldarg.0   
IL_0001: mono_ldptr2
IL_0007: calli     <object>
IL_000c: mono_ldptr_int_req_flag
IL_000e: ldind.u4  
IL_000f: brfalse   IL_0030
IL_0014: mono_not_taken
IL_0016: mono_icall <mono_thread_interruption_checkpoint>
IL_001c: dup       
IL_001d: brfalse   IL_002f
IL_0022: dup       
IL_0023: mono_objaddr
IL_0025: ldc.i4    136
IL_002a: add       
IL_002b: ldc.i4.1  
IL_002c: stind.i4  
IL_002d: mono_rethrow
IL_002f: pop       
IL_0030: ret       
// (wrapper managed-to-native) System.Configuration.InternalConfigurationHost:get_bundled_machine_config ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) object:__icall_wrapper_ves_icall_object_new_specific (intptr)
IL_0000: ldarg.0   
IL_0001: mono_jit_icall_addr2
IL_0007: calli     <intptr>
IL_000c: mono_ldptr_int_req_flag
IL_000e: ldind.u4  
IL_000f: brfalse   IL_0030
IL_0014: mono_not_taken
IL_0016: mono_icall <mono_thread_interruption_checkpoint>
IL_001c: dup       
IL_001d: brfalse   IL_002f
IL_0022: dup       
IL_0023: mono_objaddr
IL_0025: ldc.i4    136
IL_002a: add       
IL_002b: ldc.i4.1  
IL_002c: stind.i4  
IL_002d: mono_rethrow
IL_002f: pop       
IL_0030: ret       
// (wrapper managed-to-native) object:__icall_wrapper_mono_gc_alloc_vector (intptr,intptr,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: mono_jit_icall_addr2
IL_0009: calli     <intptr,intptr,intptr>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) System.GC:register_ephemeron_array (System.Runtime.CompilerServices.Ephemeron[])
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <Ephemeron[]&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.GC:get_ephemeron_tombstone ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// System.Buffers.ArrayPool`1<int>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// (wrapper managed-to-native) System.IO.Path:get_temp_path ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:type_is_assignable_from (System.Type,System.Type)
IL_0000: ldarga.s  0
IL_0002: ldarga.s  1
IL_0004: ldloca.s  0
IL_0006: mono_ldptr2
IL_000c: calli     <Type&,Type&,RuntimeStructs/MonoError&>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper managed-to-native) System.RuntimeType:MakeGenericType (System.Type,System.Type[])
IL_0000: ldarga.s  0
IL_0002: ldarga.s  1
IL_0004: ldloca.s  0
IL_0006: mono_ldptr2
IL_000c: calli     <Type&,Type[]&,RuntimeStructs/MonoError&>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void__this__ (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0041
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.3   
IL_002c: calli     <>
IL_0031: leave     IL_003f
IL_0036: stloc.1   
IL_0037: ldarg.2   
IL_0038: ldloc.1   
IL_0039: stind.ref 
IL_003a: leave     IL_003f
IL_003f: ldloc.0   
IL_0040: ret       
IL_0041: mono_ldptr_int_req_flag
IL_0043: ldind.u4  
IL_0044: brfalse   IL_0065
IL_0049: mono_not_taken
IL_004b: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0051: dup       
IL_0052: brfalse   IL_0064
IL_0057: dup       
IL_0058: mono_objaddr
IL_005a: ldc.i4    136
IL_005f: add       
IL_0060: ldc.i4.1  
IL_0061: stind.i4  
IL_0062: mono_rethrow
IL_0064: pop       
IL_0065: ldarg.0   
IL_0066: ldarg.3   
IL_0067: calli     <>
IL_006c: ldloc.0   
IL_006d: ret       
// System.Buffers.ArrayPool`1<char>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// (wrapper managed-to-native) System.Array:FastCopy (System.Array,int,System.Array,int,int)
IL_0000: ldarga.s  0
IL_0002: ldarg.1   
IL_0003: ldarga.s  2
IL_0005: ldarg.3   
IL_0006: ldarg.s   4
IL_0008: ldloca.s  0
IL_000a: mono_ldptr2
IL_0010: calli     <Array&,int,Array&,int,int,RuntimeStructs/MonoError&>
IL_0015: mono_ldptr_int_req_flag
IL_0017: ldind.u4  
IL_0018: brfalse   IL_0039
IL_001d: mono_not_taken
IL_001f: mono_icall <mono_thread_interruption_checkpoint>
IL_0025: dup       
IL_0026: brfalse   IL_0038
IL_002b: dup       
IL_002c: mono_objaddr
IL_002e: ldc.i4    136
IL_0033: add       
IL_0034: ldc.i4.1  
IL_0035: stind.i4  
IL_0036: mono_rethrow
IL_0038: pop       
IL_0039: ret       
// System.Buffers.ArrayPool`1<byte>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// (wrapper managed-to-native) Interop/Sys:Stat (byte&,Interop/Sys/FileStatus&)
IL_0000: ldc.i4.0  
IL_0001: stloc.2   
IL_0002: ldloca.s  4
IL_0004: mono_icall <mono_threads_enter_gc_safe_region_unbalanced>
IL_000a: stloc.s   5
IL_000c: ldarg.0   
IL_000d: ldarg.1   
IL_000e: mono_ldptr3
IL_0014: calli     <byte&,Interop/Sys/FileStatus&>
IL_0019: mono_icall <mono_marshal_set_last_error>
IL_001f: ldloc.s   5
IL_0021: ldloca.s  4
IL_0023: mono_icall <mono_threads_exit_gc_safe_region_unbalanced>
IL_0029: stloc.3   
IL_002a: mono_ldptr_int_req_flag
IL_002c: ldind.u4  
IL_002d: brfalse   IL_004e
IL_0032: mono_not_taken
IL_0034: mono_icall <mono_thread_interruption_checkpoint>
IL_003a: dup       
IL_003b: brfalse   IL_004d
IL_0040: dup       
IL_0041: mono_objaddr
IL_0043: ldc.i4    136
IL_0048: add       
IL_0049: ldc.i4.1  
IL_004a: stind.i4  
IL_004b: mono_rethrow
IL_004d: pop       
IL_004e: ldloc.3   
IL_004f: ret       
// (wrapper remoting-invoke-with-check) System.IO.StreamReader:.ctor (string)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_001a
IL_0014: call      <(wrapper remoting-invoke) System.IO.StreamReader:.ctor (string)>
IL_0019: ret       
IL_001a: call      <System.IO.StreamReader:.ctor (string)>
IL_001f: ret       
// (wrapper remoting-invoke-with-check) System.IO.StreamReader/NullStreamReader:.ctor ()
IL_0000: ldarg.0   
IL_0001: ldarg.0   
IL_0002: mono_objaddr
IL_0004: ldind.i   
IL_0005: ldc.i4.0  
IL_0006: add       
IL_0007: ldind.i   
IL_0008: mono_classconst <TransparentProxy>
IL_000e: bne.un    IL_0019
IL_0013: call      <(wrapper remoting-invoke) System.IO.StreamReader/NullStreamReader:.ctor ()>
IL_0018: ret       
IL_0019: call      <System.IO.StreamReader/NullStreamReader:.ctor ()>
IL_001e: ret       
// (wrapper remoting-invoke-with-check) System.IO.Stream/NullStream:.ctor ()
IL_0000: ldarg.0   
IL_0001: ldarg.0   
IL_0002: mono_objaddr
IL_0004: ldind.i   
IL_0005: ldc.i4.0  
IL_0006: add       
IL_0007: ldind.i   
IL_0008: mono_classconst <TransparentProxy>
IL_000e: bne.un    IL_0019
IL_0013: call      <(wrapper remoting-invoke) System.IO.Stream/NullStream:.ctor ()>
IL_0018: ret       
IL_0019: call      <System.IO.Stream/NullStream:.ctor ()>
IL_001e: ret       
// System.Collections.Generic.GenericEqualityComparer`1<int>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Collections.Generic.EqualityComparer`1<!0>:.ctor ()>
IL_0006: ret       
// (wrapper remoting-invoke-with-check) System.IO.TextReader/NullTextReader:.ctor ()
IL_0000: ldarg.0   
IL_0001: ldarg.0   
IL_0002: mono_objaddr
IL_0004: ldind.i   
IL_0005: ldc.i4.0  
IL_0006: add       
IL_0007: ldind.i   
IL_0008: mono_classconst <TransparentProxy>
IL_000e: bne.un    IL_0019
IL_0013: call      <(wrapper remoting-invoke) System.IO.TextReader/NullTextReader:.ctor ()>
IL_0018: ret       
IL_0019: call      <System.IO.TextReader/NullTextReader:.ctor ()>
IL_001e: ret       
// (wrapper remoting-invoke-with-check) System.IO.FileStream:.ctor (string,System.IO.FileMode,System.IO.FileAccess,System.IO.FileShare,int,System.IO.FileOptions)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.3   
IL_0004: ldarg.s   4
IL_0006: ldarg.s   5
IL_0008: ldarg.s   6
IL_000a: ldarg.0   
IL_000b: mono_objaddr
IL_000d: ldind.i   
IL_000e: ldc.i4.0  
IL_000f: add       
IL_0010: ldind.i   
IL_0011: mono_classconst <TransparentProxy>
IL_0017: bne.un    IL_0022
IL_001c: call      <(wrapper remoting-invoke) System.IO.FileStream:.ctor (string,System.IO.FileMode,System.IO.FileAccess,System.IO.FileShare,int,System.IO.FileOptions)>
IL_0021: ret       
IL_0022: call      <System.IO.FileStream:.ctor (string,System.IO.FileMode,System.IO.FileAccess,System.IO.FileShare,int,System.IO.FileOptions)>
IL_0027: ret       
// (wrapper managed-to-native) System.IO.MonoIO:Open (char*,System.IO.FileMode,System.IO.FileAccess,System.IO.FileShare,System.IO.FileOptions,System.IO.MonoIOError&)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.3   
IL_0004: ldarg.s   4
IL_0006: ldarg.s   5
IL_0008: mono_ldptr2
IL_000e: calli     <char*,FileMode,FileAccess,FileShare,FileOptions,MonoIOError&>
IL_0013: mono_ldptr_int_req_flag
IL_0015: ldind.u4  
IL_0016: brfalse   IL_0037
IL_001b: mono_not_taken
IL_001d: mono_icall <mono_thread_interruption_checkpoint>
IL_0023: dup       
IL_0024: brfalse   IL_0036
IL_0029: dup       
IL_002a: mono_objaddr
IL_002c: ldc.i4    136
IL_0031: add       
IL_0032: ldc.i4.1  
IL_0033: stind.i4  
IL_0034: mono_rethrow
IL_0036: pop       
IL_0037: ret       
// (wrapper managed-to-native) System.GC:_SuppressFinalize (object)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <object&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.IO.MonoIO:GetFileType (intptr,System.IO.MonoIOError&)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: mono_ldptr2
IL_0008: calli     <intptr,MonoIOError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.IO.MonoIO:GetLength (intptr,System.IO.MonoIOError&)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: mono_ldptr2
IL_0008: calli     <intptr,MonoIOError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.IO.MonoIO:Read (intptr,byte[],int,int,System.IO.MonoIOError&)
IL_0000: ldarg.0   
IL_0001: ldarga.s  1
IL_0003: ldarg.2   
IL_0004: ldarg.3   
IL_0005: ldarg.s   4
IL_0007: ldloca.s  0
IL_0009: mono_ldptr2
IL_000f: calli     <intptr,byte[]&,int,int,MonoIOError&,RuntimeStructs/MonoError&>
IL_0014: mono_ldptr_int_req_flag
IL_0016: ldind.u4  
IL_0017: brfalse   IL_0038
IL_001c: mono_not_taken
IL_001e: mono_icall <mono_thread_interruption_checkpoint>
IL_0024: dup       
IL_0025: brfalse   IL_0037
IL_002a: dup       
IL_002b: mono_objaddr
IL_002d: ldc.i4    136
IL_0032: add       
IL_0033: ldc.i4.1  
IL_0034: stind.i4  
IL_0035: mono_rethrow
IL_0037: pop       
IL_0038: ret       
// (wrapper managed-to-native) System.Buffer:InternalBlockCopy (System.Array,int,System.Array,int,int)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.3   
IL_0004: ldarg.s   4
IL_0006: mono_ldptr2
IL_000c: calli     <Array,int,Array,int,int>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper managed-to-managed) string:.ctor (char[],int,int)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.3   
IL_0004: call      <string:CreateString (char[],int,int)>
IL_0009: ret       
// (wrapper managed-to-native) System.Array:ClearInternal (System.Array,int,int)
IL_0000: ldarga.s  0
IL_0002: ldarg.1   
IL_0003: ldarg.2   
IL_0004: ldloca.s  0
IL_0006: mono_ldptr2
IL_000c: calli     <Array&,int,int,RuntimeStructs/MonoError&>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:internal_from_name (string,System.Threading.StackCrawlMark&,System.Reflection.Assembly,bool,bool,bool)
IL_0000: ldarga.s  0
IL_0002: ldarg.1   
IL_0003: ldarga.s  2
IL_0005: ldarg.3   
IL_0006: ldarg.s   4
IL_0008: ldarg.s   5
IL_000a: ldloca.s  0
IL_000c: mono_ldptr2
IL_0012: calli     <string&,StackCrawlMark&,Assembly&,bool,bool,bool,RuntimeStructs/MonoError&>
IL_0017: mono_ldptr_int_req_flag
IL_0019: ldind.u4  
IL_001a: brfalse   IL_003b
IL_001f: mono_not_taken
IL_0021: mono_icall <mono_thread_interruption_checkpoint>
IL_0027: dup       
IL_0028: brfalse   IL_003a
IL_002d: dup       
IL_002e: mono_objaddr
IL_0030: ldc.i4    136
IL_0035: add       
IL_0036: ldc.i4.1  
IL_0037: stind.i4  
IL_0038: mono_rethrow
IL_003a: pop       
IL_003b: ret       
// (wrapper managed-to-native) System.IO.MonoIO:Close (intptr,System.IO.MonoIOError&)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: mono_ldptr2
IL_0008: calli     <intptr,MonoIOError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:is_subclass_of (intptr,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: mono_ldptr2
IL_0008: calli     <intptr,intptr>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:GetAssembly (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.MonoCustomAttrs:IsDefinedInternal (System.Reflection.ICustomAttributeProvider,System.Type)
IL_0000: ldarga.s  0
IL_0002: ldarga.s  1
IL_0004: ldloca.s  0
IL_0006: mono_ldptr2
IL_000c: calli     <ICustomAttributeProvider&,Type&,RuntimeStructs/MonoError&>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper managed-to-native) System.Security.Cryptography.RNGCryptoServiceProvider:RngOpen ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void__this__ (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0041
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.3   
IL_002c: calli     <>
IL_0031: leave     IL_003f
IL_0036: stloc.1   
IL_0037: ldarg.2   
IL_0038: ldloc.1   
IL_0039: stind.ref 
IL_003a: leave     IL_003f
IL_003f: ldloc.0   
IL_0040: ret       
IL_0041: mono_ldptr_int_req_flag
IL_0043: ldind.u4  
IL_0044: brfalse   IL_0065
IL_0049: mono_not_taken
IL_004b: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0051: dup       
IL_0052: brfalse   IL_0064
IL_0057: dup       
IL_0058: mono_objaddr
IL_005a: ldc.i4    136
IL_005f: add       
IL_0060: ldc.i4.1  
IL_0061: stind.i4  
IL_0062: mono_rethrow
IL_0064: pop       
IL_0065: ldarg.0   
IL_0066: ldarg.3   
IL_0067: calli     <>
IL_006c: ldloc.0   
IL_006d: ret       
// (wrapper managed-to-native) System.Security.Cryptography.RNGCryptoServiceProvider:RngInitialize (byte*,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <byte*,intptr,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.Security.Cryptography.RNGCryptoServiceProvider:RngGetBytes (intptr,byte*,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldloca.s  0
IL_0005: mono_ldptr2
IL_000b: calli     <intptr,byte*,intptr,RuntimeStructs/MonoError&>
IL_0010: mono_ldptr_int_req_flag
IL_0012: ldind.u4  
IL_0013: brfalse   IL_0034
IL_0018: mono_not_taken
IL_001a: mono_icall <mono_thread_interruption_checkpoint>
IL_0020: dup       
IL_0021: brfalse   IL_0033
IL_0026: dup       
IL_0027: mono_objaddr
IL_0029: ldc.i4    136
IL_002e: add       
IL_002f: ldc.i4.1  
IL_0030: stind.i4  
IL_0031: mono_rethrow
IL_0033: pop       
IL_0034: ret       
// (wrapper managed-to-native) Interop/Sys:LStat (byte&,Interop/Sys/FileStatus&)
IL_0000: ldc.i4.0  
IL_0001: stloc.2   
IL_0002: ldloca.s  4
IL_0004: mono_icall <mono_threads_enter_gc_safe_region_unbalanced>
IL_000a: stloc.s   5
IL_000c: ldarg.0   
IL_000d: ldarg.1   
IL_000e: mono_ldptr3
IL_0014: calli     <byte&,Interop/Sys/FileStatus&>
IL_0019: mono_icall <mono_marshal_set_last_error>
IL_001f: ldloc.s   5
IL_0021: ldloca.s  4
IL_0023: mono_icall <mono_threads_exit_gc_safe_region_unbalanced>
IL_0029: stloc.3   
IL_002a: mono_ldptr_int_req_flag
IL_002c: ldind.u4  
IL_002d: brfalse   IL_004e
IL_0032: mono_not_taken
IL_0034: mono_icall <mono_thread_interruption_checkpoint>
IL_003a: dup       
IL_003b: brfalse   IL_004d
IL_0040: dup       
IL_0041: mono_objaddr
IL_0043: ldc.i4    136
IL_0048: add       
IL_0049: ldc.i4.1  
IL_004a: stind.i4  
IL_004b: mono_rethrow
IL_004d: pop       
IL_004e: ldloc.3   
IL_004f: ret       
// (wrapper managed-to-native) System.Runtime.InteropServices.Marshal:GetLastWin32Error ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper managed-to-native) Interop/Sys:ConvertErrorPlatformToPal (int)
IL_0000: ldc.i4.0  
IL_0001: stloc.2   
IL_0002: ldloca.s  4
IL_0004: mono_icall <mono_threads_enter_gc_safe_region_unbalanced>
IL_000a: stloc.s   5
IL_000c: ldarg.0   
IL_000d: mono_ldptr3
IL_0013: calli     <int>
IL_0018: ldloc.s   5
IL_001a: ldloca.s  4
IL_001c: mono_icall <mono_threads_exit_gc_safe_region_unbalanced>
IL_0022: stloc.3   
IL_0023: mono_ldptr_int_req_flag
IL_0025: ldind.u4  
IL_0026: brfalse   IL_0047
IL_002b: mono_not_taken
IL_002d: mono_icall <mono_thread_interruption_checkpoint>
IL_0033: dup       
IL_0034: brfalse   IL_0046
IL_0039: dup       
IL_003a: mono_objaddr
IL_003c: ldc.i4    136
IL_0041: add       
IL_0042: ldc.i4.1  
IL_0043: stind.i4  
IL_0044: mono_rethrow
IL_0046: pop       
IL_0047: ldloc.3   
IL_0048: ret       
// (wrapper remoting-invoke-with-check) System.IO.FileStream:.ctor (string,System.IO.FileMode,System.IO.FileAccess)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.3   
IL_0004: ldarg.0   
IL_0005: mono_objaddr
IL_0007: ldind.i   
IL_0008: ldc.i4.0  
IL_0009: add       
IL_000a: ldind.i   
IL_000b: mono_classconst <TransparentProxy>
IL_0011: bne.un    IL_001c
IL_0016: call      <(wrapper remoting-invoke) System.IO.FileStream:.ctor (string,System.IO.FileMode,System.IO.FileAccess)>
IL_001b: ret       
IL_001c: call      <System.IO.FileStream:.ctor (string,System.IO.FileMode,System.IO.FileAccess)>
IL_0021: ret       
// System.Xml.XmlReader:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// (wrapper managed-to-native) System.Environment:get_TickCount ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// System.Xml.XmlReaderSettings:.cctor ()
IL_0000: ret       
// (wrapper managed-to-native) object:__icall_wrapper_mono_gc_alloc_obj (intptr,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: mono_jit_icall_addr2
IL_0008: calli     <intptr,intptr>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// <PrivateImplementationDetails>:ComputeStringHash (string)
IL_0000: ldarg.0   
IL_0001: brfalse.s IL_002a
IL_0003: ldc.i4    -2128831035
IL_0008: stloc.0   
IL_0009: ldc.i4.0  
IL_000a: stloc.1   
IL_000b: br.s      IL_0021
IL_000d: ldarg.0   
IL_000e: ldloc.1   
IL_000f: callvirt  <string:get_Chars (int)>
IL_0014: ldloc.0   
IL_0015: xor       
IL_0016: ldc.i4    16777619
IL_001b: mul       
IL_001c: stloc.0   
IL_001d: ldloc.1   
IL_001e: ldc.i4.1  
IL_001f: add       
IL_0020: stloc.1   
IL_0021: ldloc.1   
IL_0022: ldarg.0   
IL_0023: callvirt  <string:get_Length ()>
IL_0028: blt.s     IL_000d
IL_002a: ldloc.0   
IL_002b: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:GetBaseType (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.Enum:GetEnumValuesAndNames (System.RuntimeType,ulong[]&,string[]&)
IL_0000: ldarga.s  0
IL_0002: ldnull    
IL_0003: stloc.1   
IL_0004: ldloca.s  1
IL_0006: ldnull    
IL_0007: stloc.2   
IL_0008: ldloca.s  2
IL_000a: ldloca.s  0
IL_000c: mono_ldptr2
IL_0012: calli     <RuntimeType&,ulong[]&,string[]&,RuntimeStructs/MonoError&>
IL_0017: ldarg.1   
IL_0018: ldloc.1   
IL_0019: stind.ref 
IL_001a: ldarg.2   
IL_001b: ldloc.2   
IL_001c: stind.ref 
IL_001d: mono_ldptr_int_req_flag
IL_001f: ldind.u4  
IL_0020: brfalse   IL_0041
IL_0025: mono_not_taken
IL_0027: mono_icall <mono_thread_interruption_checkpoint>
IL_002d: dup       
IL_002e: brfalse   IL_0040
IL_0033: dup       
IL_0034: mono_objaddr
IL_0036: ldc.i4    136
IL_003b: add       
IL_003c: ldc.i4.1  
IL_003d: stind.i4  
IL_003e: mono_rethrow
IL_0040: pop       
IL_0041: ret       
// (wrapper managed-to-native) System.Enum:InternalBoxEnum (System.RuntimeType,long)
IL_0000: ldarga.s  0
IL_0002: ldarg.1   
IL_0003: ldloca.s  0
IL_0005: mono_ldptr2
IL_000b: calli     <RuntimeType&,long,RuntimeStructs/MonoError&>
IL_0010: mono_ldptr_int_req_flag
IL_0012: ldind.u4  
IL_0013: brfalse   IL_0034
IL_0018: mono_not_taken
IL_001a: mono_icall <mono_thread_interruption_checkpoint>
IL_0020: dup       
IL_0021: brfalse   IL_0033
IL_0026: dup       
IL_0027: mono_objaddr
IL_0029: ldc.i4    136
IL_002e: add       
IL_002f: ldc.i4.1  
IL_0030: stind.i4  
IL_0031: mono_rethrow
IL_0033: pop       
IL_0034: ret       
// System.Collections.Generic.GenericComparer`1<ulong>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Collections.Generic.Comparer`1<!0>:.ctor ()>
IL_0006: ret       
// System.Collections.Generic.ArraySortHelper`2<ulong, string>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// (wrapper managed-to-native) object:InternalGetHashCode (object)
IL_0000: ldarg.0   
IL_0001: mono_ldptr2
IL_0007: calli     <object>
IL_000c: mono_ldptr_int_req_flag
IL_000e: ldind.u4  
IL_000f: brfalse   IL_0030
IL_0014: mono_not_taken
IL_0016: mono_icall <mono_thread_interruption_checkpoint>
IL_001c: dup       
IL_001d: brfalse   IL_002f
IL_0022: dup       
IL_0023: mono_objaddr
IL_0025: ldc.i4    136
IL_002a: add       
IL_002b: ldc.i4.1  
IL_002c: stind.i4  
IL_002d: mono_rethrow
IL_002f: pop       
IL_0030: ret       
// (wrapper remoting-invoke-with-check) System.IO.StringWriter:.ctor (System.IFormatProvider)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_001a
IL_0014: call      <(wrapper remoting-invoke) System.IO.StringWriter:.ctor (System.IFormatProvider)>
IL_0019: ret       
IL_001a: call      <System.IO.StringWriter:.ctor (System.IFormatProvider)>
IL_001f: ret       
// (wrapper remoting-invoke-with-check) System.IO.TextWriter/NullTextWriter:.ctor ()
IL_0000: ldarg.0   
IL_0001: ldarg.0   
IL_0002: mono_objaddr
IL_0004: ldind.i   
IL_0005: ldc.i4.0  
IL_0006: add       
IL_0007: ldind.i   
IL_0008: mono_classconst <TransparentProxy>
IL_000e: bne.un    IL_0019
IL_0013: call      <(wrapper remoting-invoke) System.IO.TextWriter/NullTextWriter:.ctor ()>
IL_0018: ret       
IL_0019: call      <System.IO.TextWriter/NullTextWriter:.ctor ()>
IL_001e: ret       
// (wrapper managed-to-native) System.Environment:GetNewLine ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.Configuration.InternalConfigurationHost:get_bundled_app_config ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// System.Diagnostics.SystemDiagnosticsSection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.ConfigurationSection:.ctor ()>
IL_0006: ret       
// (wrapper managed-to-native) System.GC:GetCollectionCount (int)
IL_0000: ldarg.0   
IL_0001: mono_ldptr2
IL_0007: calli     <int>
IL_000c: mono_ldptr_int_req_flag
IL_000e: ldind.u4  
IL_000f: brfalse   IL_0030
IL_0014: mono_not_taken
IL_0016: mono_icall <mono_thread_interruption_checkpoint>
IL_001c: dup       
IL_001d: brfalse   IL_002f
IL_0022: dup       
IL_0023: mono_objaddr
IL_0025: ldc.i4    136
IL_002a: add       
IL_002b: ldc.i4.1  
IL_002c: stind.i4  
IL_002d: mono_rethrow
IL_002f: pop       
IL_0030: ret       
// (wrapper managed-to-native) System.Runtime.InteropServices.GCHandle:GetTargetHandle (object,int,System.Runtime.InteropServices.GCHandleType)
IL_0000: ldarga.s  0
IL_0002: ldarg.1   
IL_0003: ldarg.2   
IL_0004: ldloca.s  0
IL_0006: mono_ldptr2
IL_000c: calli     <object&,int,GCHandleType,RuntimeStructs/MonoError&>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper managed-to-native) System.MonoCustomAttrs:GetCustomAttributesInternal (System.Reflection.ICustomAttributeProvider,System.Type,bool)
IL_0000: ldarga.s  0
IL_0002: ldarga.s  1
IL_0004: ldarg.2   
IL_0005: ldloca.s  0
IL_0007: mono_ldptr2
IL_000d: calli     <ICustomAttributeProvider&,Type&,bool,RuntimeStructs/MonoError&>
IL_0012: mono_ldptr_int_req_flag
IL_0014: ldind.u4  
IL_0015: brfalse   IL_0036
IL_001a: mono_not_taken
IL_001c: mono_icall <mono_thread_interruption_checkpoint>
IL_0022: dup       
IL_0023: brfalse   IL_0035
IL_0028: dup       
IL_0029: mono_objaddr
IL_002b: ldc.i4    136
IL_0030: add       
IL_0031: ldc.i4.1  
IL_0032: stind.i4  
IL_0033: mono_rethrow
IL_0035: pop       
IL_0036: ret       
// (wrapper managed-to-native) System.Array:CreateInstanceImpl (System.Type,int[],int[])
IL_0000: ldarga.s  0
IL_0002: ldarga.s  1
IL_0004: ldarga.s  2
IL_0006: ldloca.s  0
IL_0008: mono_ldptr2
IL_000e: calli     <Type&,int[]&,int[]&,RuntimeStructs/MonoError&>
IL_0013: mono_ldptr_int_req_flag
IL_0015: ldind.u4  
IL_0016: brfalse   IL_0037
IL_001b: mono_not_taken
IL_001d: mono_icall <mono_thread_interruption_checkpoint>
IL_0023: dup       
IL_0024: brfalse   IL_0036
IL_0029: dup       
IL_002a: mono_objaddr
IL_002c: ldc.i4    136
IL_0031: add       
IL_0032: ldc.i4.1  
IL_0033: stind.i4  
IL_0034: mono_rethrow
IL_0036: pop       
IL_0037: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:GetElementType (System.RuntimeType)
IL_0000: ldarga.s  0
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper runtime-invoke) <Module>:runtime_invoke_void__this___byte (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0044
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.1   
IL_002c: ldind.i   
IL_002d: ldind.u1  
IL_002e: ldarg.3   
IL_002f: calli     <byte>
IL_0034: leave     IL_0042
IL_0039: stloc.1   
IL_003a: ldarg.2   
IL_003b: ldloc.1   
IL_003c: stind.ref 
IL_003d: leave     IL_0042
IL_0042: ldloc.0   
IL_0043: ret       
IL_0044: mono_ldptr_int_req_flag
IL_0046: ldind.u4  
IL_0047: brfalse   IL_0068
IL_004c: mono_not_taken
IL_004e: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0054: dup       
IL_0055: brfalse   IL_0067
IL_005a: dup       
IL_005b: mono_objaddr
IL_005d: ldc.i4    136
IL_0062: add       
IL_0063: ldc.i4.1  
IL_0064: stind.i4  
IL_0065: mono_rethrow
IL_0067: pop       
IL_0068: ldarg.0   
IL_0069: ldarg.1   
IL_006a: ldind.i   
IL_006b: ldind.u1  
IL_006c: ldarg.3   
IL_006d: calli     <byte>
IL_0072: ldloc.0   
IL_0073: ret       
// (wrapper managed-to-native) System.Array:GetValueImpl (System.Array,int)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldloca.s  0
IL_0011: mono_ldptr3
IL_0017: calli     <Array&,int,RuntimeStructs/MonoError&>
IL_001c: mono_ldptr_int_req_flag
IL_001e: ldind.u4  
IL_001f: brfalse   IL_0040
IL_0024: mono_not_taken
IL_0026: mono_icall <mono_thread_interruption_checkpoint>
IL_002c: dup       
IL_002d: brfalse   IL_003f
IL_0032: dup       
IL_0033: mono_objaddr
IL_0035: ldc.i4    136
IL_003a: add       
IL_003b: ldc.i4.1  
IL_003c: stind.i4  
IL_003d: mono_rethrow
IL_003f: pop       
IL_0040: ret       
// (wrapper managed-to-native) System.Array:SetValueImpl (System.Array,object,int)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarga.s  1
IL_0010: ldarg.2   
IL_0011: ldloca.s  0
IL_0013: mono_ldptr3
IL_0019: calli     <Array&,object&,int,RuntimeStructs/MonoError&>
IL_001e: mono_ldptr_int_req_flag
IL_0020: ldind.u4  
IL_0021: brfalse   IL_0042
IL_0026: mono_not_taken
IL_0028: mono_icall <mono_thread_interruption_checkpoint>
IL_002e: dup       
IL_002f: brfalse   IL_0041
IL_0034: dup       
IL_0035: mono_objaddr
IL_0037: ldc.i4    136
IL_003c: add       
IL_003d: ldc.i4.1  
IL_003e: stind.i4  
IL_003f: mono_rethrow
IL_0041: pop       
IL_0042: ret       
// (wrapper managed-to-native) System.RuntimeType:GetInterfaces (System.RuntimeType)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldloca.s  0
IL_0010: mono_ldptr3
IL_0016: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_001b: mono_ldptr_int_req_flag
IL_001d: ldind.u4  
IL_001e: brfalse   IL_003f
IL_0023: mono_not_taken
IL_0025: mono_icall <mono_thread_interruption_checkpoint>
IL_002b: dup       
IL_002c: brfalse   IL_003e
IL_0031: dup       
IL_0032: mono_objaddr
IL_0034: ldc.i4    136
IL_0039: add       
IL_003a: ldc.i4.1  
IL_003b: stind.i4  
IL_003c: mono_rethrow
IL_003e: pop       
IL_003f: ret       
// (wrapper managed-to-native) System.Array:GetLowerBound (System.Array,int)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldloca.s  0
IL_0011: mono_ldptr3
IL_0017: calli     <Array&,int,RuntimeStructs/MonoError&>
IL_001c: mono_ldptr_int_req_flag
IL_001e: ldind.u4  
IL_001f: brfalse   IL_0040
IL_0024: mono_not_taken
IL_0026: mono_icall <mono_thread_interruption_checkpoint>
IL_002c: dup       
IL_002d: brfalse   IL_003f
IL_0032: dup       
IL_0033: mono_objaddr
IL_0035: ldc.i4    136
IL_003a: add       
IL_003b: ldc.i4.1  
IL_003c: stind.i4  
IL_003d: mono_rethrow
IL_003f: pop       
IL_0040: ret       
// (wrapper managed-to-native) System.Array:GetLength (System.Array,int)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldloca.s  0
IL_0011: mono_ldptr3
IL_0017: calli     <Array&,int,RuntimeStructs/MonoError&>
IL_001c: mono_ldptr_int_req_flag
IL_001e: ldind.u4  
IL_001f: brfalse   IL_0040
IL_0024: mono_not_taken
IL_0026: mono_icall <mono_thread_interruption_checkpoint>
IL_002c: dup       
IL_002d: brfalse   IL_003f
IL_0032: dup       
IL_0033: mono_objaddr
IL_0035: ldc.i4    136
IL_003a: add       
IL_003b: ldc.i4.1  
IL_003c: stind.i4  
IL_003d: mono_rethrow
IL_003f: pop       
IL_0040: ret       
// (wrapper managed-to-native) System.RuntimeTypeHandle:IsInstanceOfType (System.RuntimeType,object)
IL_0000: ldarga.s  0
IL_0002: ldarga.s  1
IL_0004: ldloca.s  0
IL_0006: mono_ldptr2
IL_000c: calli     <RuntimeType&,object&,RuntimeStructs/MonoError&>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper managed-to-native) System.RuntimeType:GetFields_native (System.RuntimeType,intptr,System.Reflection.BindingFlags,System.RuntimeType/MemberListType)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldarg.2   
IL_0010: ldarg.3   
IL_0011: ldloca.s  0
IL_0013: mono_ldptr3
IL_0019: calli     <RuntimeType&,intptr,BindingFlags,RuntimeType/MemberListType,RuntimeStructs/MonoError&>
IL_001e: mono_ldptr_int_req_flag
IL_0020: ldind.u4  
IL_0021: brfalse   IL_0042
IL_0026: mono_not_taken
IL_0028: mono_icall <mono_thread_interruption_checkpoint>
IL_002e: dup       
IL_002f: brfalse   IL_0041
IL_0034: dup       
IL_0035: mono_objaddr
IL_0037: ldc.i4    136
IL_003c: add       
IL_003d: ldc.i4.1  
IL_003e: stind.i4  
IL_003f: mono_rethrow
IL_0041: pop       
IL_0042: ret       
// (wrapper managed-to-native) System.Reflection.FieldInfo:internal_from_handle_type (intptr,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <intptr,intptr,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.Reflection.RuntimeFieldInfo:GetParentType (System.Reflection.RuntimeFieldInfo,bool)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldloca.s  0
IL_0011: mono_ldptr3
IL_0017: calli     <RuntimeFieldInfo&,bool,RuntimeStructs/MonoError&>
IL_001c: mono_ldptr_int_req_flag
IL_001e: ldind.u4  
IL_001f: brfalse   IL_0040
IL_0024: mono_not_taken
IL_0026: mono_icall <mono_thread_interruption_checkpoint>
IL_002c: dup       
IL_002d: brfalse   IL_003f
IL_0032: dup       
IL_0033: mono_objaddr
IL_0035: ldc.i4    136
IL_003a: add       
IL_003b: ldc.i4.1  
IL_003c: stind.i4  
IL_003d: mono_rethrow
IL_003f: pop       
IL_0040: ret       
// (wrapper managed-to-native) System.Reflection.RuntimeFieldInfo:GetValueInternal (System.Reflection.RuntimeFieldInfo,object)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarg.0   
IL_000d: ldarg.1   
IL_000e: mono_ldptr3
IL_0014: calli     <RuntimeFieldInfo,object>
IL_0019: mono_ldptr_int_req_flag
IL_001b: ldind.u4  
IL_001c: brfalse   IL_003d
IL_0021: mono_not_taken
IL_0023: mono_icall <mono_thread_interruption_checkpoint>
IL_0029: dup       
IL_002a: brfalse   IL_003c
IL_002f: dup       
IL_0030: mono_objaddr
IL_0032: ldc.i4    136
IL_0037: add       
IL_0038: ldc.i4.1  
IL_0039: stind.i4  
IL_003a: mono_rethrow
IL_003c: pop       
IL_003d: ret       
// System.SecurityUtils:.cctor ()
IL_0000: ret       
// (wrapper managed-to-native) System.RuntimeType:get_DeclaringType (System.RuntimeType)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldloca.s  0
IL_0010: mono_ldptr3
IL_0016: calli     <RuntimeType&,RuntimeStructs/MonoError&>
IL_001b: mono_ldptr_int_req_flag
IL_001d: ldind.u4  
IL_001e: brfalse   IL_003f
IL_0023: mono_not_taken
IL_0025: mono_icall <mono_thread_interruption_checkpoint>
IL_002b: dup       
IL_002c: brfalse   IL_003e
IL_0031: dup       
IL_0032: mono_objaddr
IL_0034: ldc.i4    136
IL_0039: add       
IL_003a: ldc.i4.1  
IL_003b: stind.i4  
IL_003c: mono_rethrow
IL_003e: pop       
IL_003f: ret       
// System.ComponentModel.BooleanConverter:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.ComponentModel.TypeConverter:.ctor ()>
IL_0006: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void__this__ (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0041
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.3   
IL_002c: calli     <>
IL_0031: leave     IL_003f
IL_0036: stloc.1   
IL_0037: ldarg.2   
IL_0038: ldloc.1   
IL_0039: stind.ref 
IL_003a: leave     IL_003f
IL_003f: ldloc.0   
IL_0040: ret       
IL_0041: mono_ldptr_int_req_flag
IL_0043: ldind.u4  
IL_0044: brfalse   IL_0065
IL_0049: mono_not_taken
IL_004b: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0051: dup       
IL_0052: brfalse   IL_0064
IL_0057: dup       
IL_0058: mono_objaddr
IL_005a: ldc.i4    136
IL_005f: add       
IL_0060: ldc.i4.1  
IL_0061: stind.i4  
IL_0062: mono_rethrow
IL_0064: pop       
IL_0065: ldarg.0   
IL_0066: ldarg.3   
IL_0067: calli     <>
IL_006c: ldloc.0   
IL_006d: ret       
// System.ComponentModel.TypeConverter:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// System.ComponentModel.TypeConverter:.cctor ()
IL_0000: ret       
// System.ComponentModel.StringConverter:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.ComponentModel.TypeConverter:.ctor ()>
IL_0006: ret       
// (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0040
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.3   
IL_002b: calli     <>
IL_0030: leave     IL_003e
IL_0035: stloc.1   
IL_0036: ldarg.2   
IL_0037: ldloc.1   
IL_0038: stind.ref 
IL_0039: leave     IL_003e
IL_003e: ldloc.0   
IL_003f: ret       
IL_0040: mono_ldptr_int_req_flag
IL_0042: ldind.u4  
IL_0043: brfalse   IL_0064
IL_0048: mono_not_taken
IL_004a: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0050: dup       
IL_0051: brfalse   IL_0063
IL_0056: dup       
IL_0057: mono_objaddr
IL_0059: ldc.i4    136
IL_005e: add       
IL_005f: ldc.i4.1  
IL_0060: stind.i4  
IL_0061: mono_rethrow
IL_0063: pop       
IL_0064: ldarg.3   
IL_0065: calli     <>
IL_006a: ldloc.0   
IL_006b: ret       
// System.Diagnostics.AssertSection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.ConfigurationElement:.ctor ()>
IL_0006: ret       
// System.ComponentModel.Int32Converter:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.ComponentModel.BaseNumberConverter:.ctor ()>
IL_0006: ret       
// System.Diagnostics.PerfCounterSection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.ConfigurationElement:.ctor ()>
IL_0006: ret       
// System.Diagnostics.SourceElementsCollection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.ConfigurationElementCollection:.ctor ()>
IL_0006: ret       
// (wrapper runtime-invoke) <Module>:runtime_invoke_void__this___object (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0043
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.1   
IL_002c: ldind.ref 
IL_002d: ldarg.3   
IL_002e: calli     <object>
IL_0033: leave     IL_0041
IL_0038: stloc.1   
IL_0039: ldarg.2   
IL_003a: ldloc.1   
IL_003b: stind.ref 
IL_003c: leave     IL_0041
IL_0041: ldloc.0   
IL_0042: ret       
IL_0043: mono_ldptr_int_req_flag
IL_0045: ldind.u4  
IL_0046: brfalse   IL_0067
IL_004b: mono_not_taken
IL_004d: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0053: dup       
IL_0054: brfalse   IL_0066
IL_0059: dup       
IL_005a: mono_objaddr
IL_005c: ldc.i4    136
IL_0061: add       
IL_0062: ldc.i4.1  
IL_0063: stind.i4  
IL_0064: mono_rethrow
IL_0066: pop       
IL_0067: ldarg.0   
IL_0068: ldarg.1   
IL_0069: ldind.ref 
IL_006a: ldarg.3   
IL_006b: calli     <object>
IL_0070: ldloc.0   
IL_0071: ret       
// (wrapper runtime-invoke) <Module>:runtime_invoke_void__this___int (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0044
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.1   
IL_002c: ldind.i   
IL_002d: ldind.i4  
IL_002e: ldarg.3   
IL_002f: calli     <int>
IL_0034: leave     IL_0042
IL_0039: stloc.1   
IL_003a: ldarg.2   
IL_003b: ldloc.1   
IL_003c: stind.ref 
IL_003d: leave     IL_0042
IL_0042: ldloc.0   
IL_0043: ret       
IL_0044: mono_ldptr_int_req_flag
IL_0046: ldind.u4  
IL_0047: brfalse   IL_0068
IL_004c: mono_not_taken
IL_004e: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0054: dup       
IL_0055: brfalse   IL_0067
IL_005a: dup       
IL_005b: mono_objaddr
IL_005d: ldc.i4    136
IL_0062: add       
IL_0063: ldc.i4.1  
IL_0064: stind.i4  
IL_0065: mono_rethrow
IL_0067: pop       
IL_0068: ldarg.0   
IL_0069: ldarg.1   
IL_006a: ldind.i   
IL_006b: ldind.i4  
IL_006c: ldarg.3   
IL_006d: calli     <int>
IL_0072: ldloc.0   
IL_0073: ret       
// System.ComponentModel.CollectionConverter:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.ComponentModel.TypeConverter:.ctor ()>
IL_0006: ret       
// System.Diagnostics.SharedListenerElementsCollection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Diagnostics.ListenerElementsCollection:.ctor ()>
IL_0006: ret       
// System.Diagnostics.ListenerElementsCollection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.ConfigurationElementCollection:.ctor ()>
IL_0006: ret       
// System.Diagnostics.SwitchElementsCollection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.ConfigurationElementCollection:.ctor ()>
IL_0006: ret       
// System.Diagnostics.TraceSection:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Configuration.ConfigurationElement:.ctor ()>
IL_0006: ret       
// (wrapper runtime-invoke) <Module>:runtime_invoke_void__this___int (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0044
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.1   
IL_002c: ldind.i   
IL_002d: ldind.i4  
IL_002e: ldarg.3   
IL_002f: calli     <int>
IL_0034: leave     IL_0042
IL_0039: stloc.1   
IL_003a: ldarg.2   
IL_003b: ldloc.1   
IL_003c: stind.ref 
IL_003d: leave     IL_0042
IL_0042: ldloc.0   
IL_0043: ret       
IL_0044: mono_ldptr_int_req_flag
IL_0046: ldind.u4  
IL_0047: brfalse   IL_0068
IL_004c: mono_not_taken
IL_004e: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0054: dup       
IL_0055: brfalse   IL_0067
IL_005a: dup       
IL_005b: mono_objaddr
IL_005d: ldc.i4    136
IL_0062: add       
IL_0063: ldc.i4.1  
IL_0064: stind.i4  
IL_0065: mono_rethrow
IL_0067: pop       
IL_0068: ldarg.0   
IL_0069: ldarg.1   
IL_006a: ldind.i   
IL_006b: ldind.i4  
IL_006c: ldarg.3   
IL_006d: calli     <int>
IL_0072: ldloc.0   
IL_0073: ret       
// (wrapper managed-to-native) System.RuntimeType:GetPropertiesByName_native (System.RuntimeType,intptr,System.Reflection.BindingFlags,System.RuntimeType/MemberListType)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldarg.2   
IL_0010: ldarg.3   
IL_0011: ldloca.s  0
IL_0013: mono_ldptr3
IL_0019: calli     <RuntimeType&,intptr,BindingFlags,RuntimeType/MemberListType,RuntimeStructs/MonoError&>
IL_001e: mono_ldptr_int_req_flag
IL_0020: ldind.u4  
IL_0021: brfalse   IL_0042
IL_0026: mono_not_taken
IL_0028: mono_icall <mono_thread_interruption_checkpoint>
IL_002e: dup       
IL_002f: brfalse   IL_0041
IL_0034: dup       
IL_0035: mono_objaddr
IL_0037: ldc.i4    136
IL_003c: add       
IL_003d: ldc.i4.1  
IL_003e: stind.i4  
IL_003f: mono_rethrow
IL_0041: pop       
IL_0042: ret       
// (wrapper managed-to-native) System.Reflection.RuntimePropertyInfo:internal_from_handle_type (intptr,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <intptr,intptr,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper managed-to-native) System.Reflection.RuntimePropertyInfo:get_property_info (System.Reflection.RuntimePropertyInfo,System.Reflection.MonoPropertyInfo&,System.Reflection.PInfo)
IL_0000: ldarga.s  0
IL_0002: ldarg.1   
IL_0003: ldarg.2   
IL_0004: ldloca.s  0
IL_0006: mono_ldptr2
IL_000c: calli     <RuntimePropertyInfo&,MonoPropertyInfo&,PInfo,RuntimeStructs/MonoError&>
IL_0011: mono_ldptr_int_req_flag
IL_0013: ldind.u4  
IL_0014: brfalse   IL_0035
IL_0019: mono_not_taken
IL_001b: mono_icall <mono_thread_interruption_checkpoint>
IL_0021: dup       
IL_0022: brfalse   IL_0034
IL_0027: dup       
IL_0028: mono_objaddr
IL_002a: ldc.i4    136
IL_002f: add       
IL_0030: ldc.i4.1  
IL_0031: stind.i4  
IL_0032: mono_rethrow
IL_0034: pop       
IL_0035: ret       
// (wrapper managed-to-native) System.Reflection.RuntimeMethodInfo:get_base_method (System.Reflection.RuntimeMethodInfo,bool)
IL_0000: ldarga.s  0
IL_0002: ldarg.1   
IL_0003: ldloca.s  0
IL_0005: mono_ldptr2
IL_000b: calli     <RuntimeMethodInfo&,bool,RuntimeStructs/MonoError&>
IL_0010: mono_ldptr_int_req_flag
IL_0012: ldind.u4  
IL_0013: brfalse   IL_0034
IL_0018: mono_not_taken
IL_001a: mono_icall <mono_thread_interruption_checkpoint>
IL_0020: dup       
IL_0021: brfalse   IL_0033
IL_0026: dup       
IL_0027: mono_objaddr
IL_0029: ldc.i4    136
IL_002e: add       
IL_002f: ldc.i4.1  
IL_0030: stind.i4  
IL_0031: mono_rethrow
IL_0033: pop       
IL_0034: ret       
// (wrapper managed-to-native) System.Reflection.MonoMethodInfo:get_method_info (intptr,System.Reflection.MonoMethodInfo&)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldloca.s  0
IL_0004: mono_ldptr2
IL_000a: calli     <intptr,MonoMethodInfo&,RuntimeStructs/MonoError&>
IL_000f: mono_ldptr_int_req_flag
IL_0011: ldind.u4  
IL_0012: brfalse   IL_0033
IL_0017: mono_not_taken
IL_0019: mono_icall <mono_thread_interruption_checkpoint>
IL_001f: dup       
IL_0020: brfalse   IL_0032
IL_0025: dup       
IL_0026: mono_objaddr
IL_0028: ldc.i4    136
IL_002d: add       
IL_002e: ldc.i4.1  
IL_002f: stind.i4  
IL_0030: mono_rethrow
IL_0032: pop       
IL_0033: ret       
// (wrapper runtime-invoke) <Module>:runtime_invoke_void__this___object (object,intptr,intptr,intptr)
IL_0000: ldarg.2   
IL_0001: brfalse   IL_0043
IL_0006: mono_ldptr_int_req_flag
IL_0008: ldind.u4  
IL_0009: brfalse   IL_002a
IL_000e: mono_not_taken
IL_0010: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0016: dup       
IL_0017: brfalse   IL_0029
IL_001c: dup       
IL_001d: mono_objaddr
IL_001f: ldc.i4    136
IL_0024: add       
IL_0025: ldc.i4.1  
IL_0026: stind.i4  
IL_0027: mono_rethrow
IL_0029: pop       
IL_002a: ldarg.0   
IL_002b: ldarg.1   
IL_002c: ldind.ref 
IL_002d: ldarg.3   
IL_002e: calli     <object>
IL_0033: leave     IL_0041
IL_0038: stloc.1   
IL_0039: ldarg.2   
IL_003a: ldloc.1   
IL_003b: stind.ref 
IL_003c: leave     IL_0041
IL_0041: ldloc.0   
IL_0042: ret       
IL_0043: mono_ldptr_int_req_flag
IL_0045: ldind.u4  
IL_0046: brfalse   IL_0067
IL_004b: mono_not_taken
IL_004d: mono_icall <mono_thread_force_interruption_checkpoint_noraise>
IL_0053: dup       
IL_0054: brfalse   IL_0066
IL_0059: dup       
IL_005a: mono_objaddr
IL_005c: ldc.i4    136
IL_0061: add       
IL_0062: ldc.i4.1  
IL_0063: stind.i4  
IL_0064: mono_rethrow
IL_0066: pop       
IL_0067: ldarg.0   
IL_0068: ldarg.1   
IL_0069: ldind.ref 
IL_006a: ldarg.3   
IL_006b: calli     <object>
IL_0070: ldloc.0   
IL_0071: ret       
// (wrapper managed-to-native) System.RuntimeType:getFullName (System.RuntimeType,bool,bool)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarga.s  0
IL_000e: ldarg.1   
IL_000f: ldarg.2   
IL_0010: ldloca.s  0
IL_0012: mono_ldptr3
IL_0018: calli     <RuntimeType&,bool,bool,RuntimeStructs/MonoError&>
IL_001d: mono_ldptr_int_req_flag
IL_001f: ldind.u4  
IL_0020: brfalse   IL_0041
IL_0025: mono_not_taken
IL_0027: mono_icall <mono_thread_interruption_checkpoint>
IL_002d: dup       
IL_002e: brfalse   IL_0040
IL_0033: dup       
IL_0034: mono_objaddr
IL_0036: ldc.i4    136
IL_003b: add       
IL_003c: ldc.i4.1  
IL_003d: stind.i4  
IL_003e: mono_rethrow
IL_0040: pop       
IL_0041: ret       
// (wrapper remoting-invoke-with-check) System.IO.StringReader:.ctor (string)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_001a
IL_0014: call      <(wrapper remoting-invoke) System.IO.StringReader:.ctor (string)>
IL_0019: ret       
IL_001a: call      <System.IO.StringReader:.ctor (string)>
IL_001f: ret       
// (wrapper managed-to-native) System.Security.SecurityManager:get_SecurityEnabled ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper remoting-invoke-with-check) System.Diagnostics.TraceListener:SetAttributes (System.Collections.Hashtable)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_0033
IL_0014: ldarg.0   
IL_0015: mono_objaddr
IL_0017: ldc.i4.s  16
IL_0019: add       
IL_001a: ldind.ref 
IL_001b: mono_objaddr
IL_001d: ldc.i4.s  40
IL_001f: add       
IL_0020: ldind.i4  
IL_0021: ldc.i4.m1 
IL_0022: beq       IL_002d
IL_0027: call      <(wrapper xdomain-invoke) System.Diagnostics.TraceListener:SetAttributes (System.Collections.Hashtable)>
IL_002c: ret       
IL_002d: call      <(wrapper remoting-invoke) System.Diagnostics.TraceListener:SetAttributes (System.Collections.Hashtable)>
IL_0032: ret       
IL_0033: call      <System.Diagnostics.TraceListener:SetAttributes (System.Collections.Hashtable)>
IL_0038: ret       
// (wrapper remoting-invoke-with-check) System.Diagnostics.TraceListener:set_TraceOutputOptions (System.Diagnostics.TraceOptions)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_0033
IL_0014: ldarg.0   
IL_0015: mono_objaddr
IL_0017: ldc.i4.s  16
IL_0019: add       
IL_001a: ldind.ref 
IL_001b: mono_objaddr
IL_001d: ldc.i4.s  40
IL_001f: add       
IL_0020: ldind.i4  
IL_0021: ldc.i4.m1 
IL_0022: beq       IL_002d
IL_0027: call      <(wrapper xdomain-invoke) System.Diagnostics.TraceListener:set_TraceOutputOptions (System.Diagnostics.TraceOptions)>
IL_002c: ret       
IL_002d: call      <(wrapper remoting-invoke) System.Diagnostics.TraceListener:set_TraceOutputOptions (System.Diagnostics.TraceOptions)>
IL_0032: ret       
IL_0033: call      <System.Diagnostics.TraceListener:set_TraceOutputOptions (System.Diagnostics.TraceOptions)>
IL_0038: ret       
// (wrapper remoting-invoke-with-check) System.Diagnostics.TraceListener:set_IndentSize (int)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_0033
IL_0014: ldarg.0   
IL_0015: mono_objaddr
IL_0017: ldc.i4.s  16
IL_0019: add       
IL_001a: ldind.ref 
IL_001b: mono_objaddr
IL_001d: ldc.i4.s  40
IL_001f: add       
IL_0020: ldind.i4  
IL_0021: ldc.i4.m1 
IL_0022: beq       IL_002d
IL_0027: call      <(wrapper xdomain-invoke) System.Diagnostics.TraceListener:set_IndentSize (int)>
IL_002c: ret       
IL_002d: call      <(wrapper remoting-invoke) System.Diagnostics.TraceListener:set_IndentSize (int)>
IL_0032: ret       
IL_0033: call      <System.Diagnostics.TraceListener:set_IndentSize (int)>
IL_0038: ret       
// (wrapper remoting-invoke-with-check) System.Diagnostics.TraceListener:set_IndentLevel (int)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_0033
IL_0014: ldarg.0   
IL_0015: mono_objaddr
IL_0017: ldc.i4.s  16
IL_0019: add       
IL_001a: ldind.ref 
IL_001b: mono_objaddr
IL_001d: ldc.i4.s  40
IL_001f: add       
IL_0020: ldind.i4  
IL_0021: ldc.i4.m1 
IL_0022: beq       IL_002d
IL_0027: call      <(wrapper xdomain-invoke) System.Diagnostics.TraceListener:set_IndentLevel (int)>
IL_002c: ret       
IL_002d: call      <(wrapper remoting-invoke) System.Diagnostics.TraceListener:set_IndentLevel (int)>
IL_0032: ret       
IL_0033: call      <System.Diagnostics.TraceListener:set_IndentLevel (int)>
IL_0038: ret       
// (wrapper remoting-invoke-with-check) System.Diagnostics.ConsoleTraceListener:.ctor ()
IL_0000: ldarg.0   
IL_0001: ldarg.0   
IL_0002: mono_objaddr
IL_0004: ldind.i   
IL_0005: ldc.i4.0  
IL_0006: add       
IL_0007: ldind.i   
IL_0008: mono_classconst <TransparentProxy>
IL_000e: bne.un    IL_0019
IL_0013: call      <(wrapper remoting-invoke) System.Diagnostics.ConsoleTraceListener:.ctor ()>
IL_0018: ret       
IL_0019: call      <System.Diagnostics.ConsoleTraceListener:.ctor ()>
IL_001e: ret       
// (wrapper managed-to-native) System.Text.EncodingHelper:InternalCodePage (int&)
IL_0000: ldarg.0   
IL_0001: ldloca.s  0
IL_0003: mono_ldptr2
IL_0009: calli     <int&,RuntimeStructs/MonoError&>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) System.IO.MonoIO:get_ConsoleOutput ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper managed-to-native) System.ConsoleDriver:Isatty (intptr)
IL_0000: ldarg.0   
IL_0001: ldloca.s  0
IL_0003: mono_ldptr2
IL_0009: calli     <intptr,RuntimeStructs/MonoError&>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) System.IO.MonoIO:get_ConsoleInput ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// (wrapper remoting-invoke-with-check) System.IO.FileStream:.ctor (intptr,System.IO.FileAccess,bool,int,bool,bool)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.3   
IL_0004: ldarg.s   4
IL_0006: ldarg.s   5
IL_0008: ldarg.s   6
IL_000a: ldarg.0   
IL_000b: mono_objaddr
IL_000d: ldind.i   
IL_000e: ldc.i4.0  
IL_000f: add       
IL_0010: ldind.i   
IL_0011: mono_classconst <TransparentProxy>
IL_0017: bne.un    IL_0022
IL_001c: call      <(wrapper remoting-invoke) System.IO.FileStream:.ctor (intptr,System.IO.FileAccess,bool,int,bool,bool)>
IL_0021: ret       
IL_0022: call      <System.IO.FileStream:.ctor (intptr,System.IO.FileAccess,bool,int,bool,bool)>
IL_0027: ret       
// (wrapper remoting-invoke-with-check) System.IO.UnexceptionalStreamReader:.ctor (System.IO.Stream,System.Text.Encoding)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.0   
IL_0004: mono_objaddr
IL_0006: ldind.i   
IL_0007: ldc.i4.0  
IL_0008: add       
IL_0009: ldind.i   
IL_000a: mono_classconst <TransparentProxy>
IL_0010: bne.un    IL_001b
IL_0015: call      <(wrapper remoting-invoke) System.IO.UnexceptionalStreamReader:.ctor (System.IO.Stream,System.Text.Encoding)>
IL_001a: ret       
IL_001b: call      <System.IO.UnexceptionalStreamReader:.ctor (System.IO.Stream,System.Text.Encoding)>
IL_0020: ret       
// (wrapper remoting-invoke-with-check) System.IO.TextReader/SyncTextReader:.ctor (System.IO.TextReader)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_001a
IL_0014: call      <(wrapper remoting-invoke) System.IO.TextReader/SyncTextReader:.ctor (System.IO.TextReader)>
IL_0019: ret       
IL_001a: call      <System.IO.TextReader/SyncTextReader:.ctor (System.IO.TextReader)>
IL_001f: ret       
// (wrapper remoting-invoke-with-check) System.IO.UnexceptionalStreamWriter:.ctor (System.IO.Stream,System.Text.Encoding)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.0   
IL_0004: mono_objaddr
IL_0006: ldind.i   
IL_0007: ldc.i4.0  
IL_0008: add       
IL_0009: ldind.i   
IL_000a: mono_classconst <TransparentProxy>
IL_0010: bne.un    IL_001b
IL_0015: call      <(wrapper remoting-invoke) System.IO.UnexceptionalStreamWriter:.ctor (System.IO.Stream,System.Text.Encoding)>
IL_001a: ret       
IL_001b: call      <System.IO.UnexceptionalStreamWriter:.ctor (System.IO.Stream,System.Text.Encoding)>
IL_0020: ret       
// (wrapper remoting-invoke-with-check) System.IO.StreamWriter:.ctor (System.IO.Stream,System.Text.Encoding,int,bool)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: ldarg.3   
IL_0004: ldarg.s   4
IL_0006: ldarg.0   
IL_0007: mono_objaddr
IL_0009: ldind.i   
IL_000a: ldc.i4.0  
IL_000b: add       
IL_000c: ldind.i   
IL_000d: mono_classconst <TransparentProxy>
IL_0013: bne.un    IL_001e
IL_0018: call      <(wrapper remoting-invoke) System.IO.StreamWriter:.ctor (System.IO.Stream,System.Text.Encoding,int,bool)>
IL_001d: ret       
IL_001e: call      <System.IO.StreamWriter:.ctor (System.IO.Stream,System.Text.Encoding,int,bool)>
IL_0023: ret       
// (wrapper remoting-invoke-with-check) System.IO.TextWriter/SyncTextWriter:.ctor (System.IO.TextWriter)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_001a
IL_0014: call      <(wrapper remoting-invoke) System.IO.TextWriter/SyncTextWriter:.ctor (System.IO.TextWriter)>
IL_0019: ret       
IL_001a: call      <System.IO.TextWriter/SyncTextWriter:.ctor (System.IO.TextWriter)>
IL_001f: ret       
// (wrapper managed-to-native) System.Globalization.CultureInfo:get_current_locale_name ()
IL_0000: ldloca.s  0
IL_0002: mono_ldptr2
IL_0008: calli     <RuntimeStructs/MonoError&>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// (wrapper managed-to-native) System.Globalization.CultureInfo:construct_internal_locale_from_name (System.Globalization.CultureInfo,string)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarg.0   
IL_000d: ldarg.1   
IL_000e: mono_ldptr3
IL_0014: calli     <CultureInfo,string>
IL_0019: mono_ldptr_int_req_flag
IL_001b: ldind.u4  
IL_001c: brfalse   IL_003d
IL_0021: mono_not_taken
IL_0023: mono_icall <mono_thread_interruption_checkpoint>
IL_0029: dup       
IL_002a: brfalse   IL_003c
IL_002f: dup       
IL_0030: mono_objaddr
IL_0032: ldc.i4    136
IL_0037: add       
IL_0038: ldc.i4.1  
IL_0039: stind.i4  
IL_003a: mono_rethrow
IL_003c: pop       
IL_003d: ret       
// (wrapper managed-to-native) System.Globalization.CultureData:fill_culture_data (System.Globalization.CultureData,int)
IL_0000: ldarg.0   
IL_0001: brtrue    IL_000c
IL_0006: newobj    <System.NullReferenceException:.ctor ()>
IL_000b: throw     
IL_000c: ldarg.0   
IL_000d: ldarg.1   
IL_000e: mono_ldptr3
IL_0014: calli     <CultureData,int>
IL_0019: mono_ldptr_int_req_flag
IL_001b: ldind.u4  
IL_001c: brfalse   IL_003d
IL_0021: mono_not_taken
IL_0023: mono_icall <mono_thread_interruption_checkpoint>
IL_0029: dup       
IL_002a: brfalse   IL_003c
IL_002f: dup       
IL_0030: mono_objaddr
IL_0032: ldc.i4    136
IL_0037: add       
IL_0038: ldc.i4.1  
IL_0039: stind.i4  
IL_003a: mono_rethrow
IL_003c: pop       
IL_003d: ret       
// (wrapper managed-to-native) System.IO.MonoIO:get_ConsoleError ()
IL_0000: mono_ldptr2
IL_0006: calli     <>
IL_000b: mono_ldptr_int_req_flag
IL_000d: ldind.u4  
IL_000e: brfalse   IL_002f
IL_0013: mono_not_taken
IL_0015: mono_icall <mono_thread_interruption_checkpoint>
IL_001b: dup       
IL_001c: brfalse   IL_002e
IL_0021: dup       
IL_0022: mono_objaddr
IL_0024: ldc.i4    136
IL_0029: add       
IL_002a: ldc.i4.1  
IL_002b: stind.i4  
IL_002c: mono_rethrow
IL_002e: pop       
IL_002f: ret       
// System.Diagnostics.Trace:.cctor ()
IL_0000: ret       
// (wrapper remoting-invoke-with-check) System.IO.StreamReader:.ctor (System.IO.Stream)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_001a
IL_0014: call      <(wrapper remoting-invoke) System.IO.StreamReader:.ctor (System.IO.Stream)>
IL_0019: ret       
IL_001a: call      <System.IO.StreamReader:.ctor (System.IO.Stream)>
IL_001f: ret       
// (wrapper remoting-invoke-with-check) System.IO.StreamWriter:.ctor (System.IO.Stream)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.0   
IL_0003: mono_objaddr
IL_0005: ldind.i   
IL_0006: ldc.i4.0  
IL_0007: add       
IL_0008: ldind.i   
IL_0009: mono_classconst <TransparentProxy>
IL_000f: bne.un    IL_001a
IL_0014: call      <(wrapper remoting-invoke) System.IO.StreamWriter:.ctor (System.IO.Stream)>
IL_0019: ret       
IL_001a: call      <System.IO.StreamWriter:.ctor (System.IO.Stream)>
IL_001f: ret       
// (wrapper castclass) object:__isinst_with_cache (object,intptr,intptr)
IL_0000: ldarg.0   
IL_0001: brfalse   IL_0034
IL_0006: ldarg.0   
IL_0007: mono_objaddr
IL_0009: ldind.i   
IL_000a: stloc.0   
IL_000b: ldarg.2   
IL_000c: ldind.i   
IL_000d: stloc.1   
IL_000e: ldloc.1   
IL_000f: ldc.i4    -2
IL_0014: conv.i    
IL_0015: and       
IL_0016: ldloc.0   
IL_0017: bne.un    IL_002a
IL_001c: ldloc.1   
IL_001d: ldc.i4.1  
IL_001e: conv.u    
IL_001f: and       
IL_0020: brtrue    IL_0034
IL_0025: br        IL_0036
IL_002a: ldarg.0   
IL_002b: ldarg.1   
IL_002c: ldarg.2   
IL_002d: mono_icall <mono_marshal_isinst_with_cache>
IL_0033: ret       
IL_0034: ldnull    
IL_0035: ret       
IL_0036: ldarg.0   
IL_0037: ret       
// (wrapper managed-to-native) object:__icall_wrapper_mono_marshal_isinst_with_cache (object,intptr,intptr)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: ldarg.2   
IL_0003: mono_jit_icall_addr2
IL_0009: calli     <object,intptr,intptr>
IL_000e: mono_ldptr_int_req_flag
IL_0010: ldind.u4  
IL_0011: brfalse   IL_0032
IL_0016: mono_not_taken
IL_0018: mono_icall <mono_thread_interruption_checkpoint>
IL_001e: dup       
IL_001f: brfalse   IL_0031
IL_0024: dup       
IL_0025: mono_objaddr
IL_0027: ldc.i4    136
IL_002c: add       
IL_002d: ldc.i4.1  
IL_002e: stind.i4  
IL_002f: mono_rethrow
IL_0031: pop       
IL_0032: ret       
// (wrapper managed-to-native) System.Globalization.CultureData:fill_number_data (System.Globalization.NumberFormatInfo,int)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: mono_ldptr2
IL_0008: calli     <NumberFormatInfo,int>
IL_000d: mono_ldptr_int_req_flag
IL_000f: ldind.u4  
IL_0010: brfalse   IL_0031
IL_0015: mono_not_taken
IL_0017: mono_icall <mono_thread_interruption_checkpoint>
IL_001d: dup       
IL_001e: brfalse   IL_0030
IL_0023: dup       
IL_0024: mono_objaddr
IL_0026: ldc.i4    136
IL_002b: add       
IL_002c: ldc.i4.1  
IL_002d: stind.i4  
IL_002e: mono_rethrow
IL_0030: pop       
IL_0031: ret       
// System.Collections.Generic.ArraySortHelper`1<int>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// System.Collections.Generic.GenericComparer`1<int>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <System.Collections.Generic.Comparer`1<!0>:.ctor ()>
IL_0006: ret       
// System.Collections.Generic.ArraySortHelper`2<int, int>:.ctor ()
IL_0000: ldarg.0   
IL_0001: call      <object:.ctor ()>
IL_0006: ret       
// (wrapper managed-to-managed) int[]:System.Collections.Generic.IList`1.get_Item (int)
IL_0000: ldarg.0   
IL_0001: ldarg.1   
IL_0002: call      <System.Array:InternalArray__get_Item<int> (int)>
IL_0007: ret       
