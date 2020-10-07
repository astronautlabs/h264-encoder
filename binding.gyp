{
    "targets": [
        {
            "target_name" : "h264encoder",
            'include_dirs': [
                "<!(node -p \"require('node-addon-api').include_dir\")",
                "external/minih264/include"
            ],
            'sources' : [
                "external/minih264/system.c",
                "src/init.cc",
                "src/version.cc"
            ],
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'xcode_settings': {
                'GCC_ENABLE_CPP_RTTI': 'YES',
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'MACOSX_DEPLOYMENT_TARGET': '10.7',
                'CLANG_CXX_LIBRARY': 'libc++',
                'OTHER_CPLUSPLUSFLAGS': [
                    '-std=c++11',
                    '-stdlib=libc++'
                ]
            },

            "conditions": [
                [
                    'OS=="mac"', 
                    {
                        "link_settings": {
                            "ldflags" : [
                                "-lm -ldl -lpthread"
                            ]
                        }
                    }
                ],
                [
                    'OS=="linux"', 
                    {
                        'link_settings' : {
                            "ldflags" : [
                                "-lm -ldl -lpthread"
                            ]
                        }
                    }
                ],
                [
                    'OS=="win"', 
                    {
                        "configurations": {
                            "Release": {
                                "msvs_settings": {
                                    "VCCLCompilerTool": {
                                        "RuntimeTypeInfo": "true",
                                        "ExceptionHandling": 1,
                                        'AdditionalOptions': [ '/Ob2', '/DH264E_MAX_THREADS=0', '/TP' ],
                                        'RuntimeLibrary': 3
                                    },
                                    'VCLinkerTool': {
                                        'AdditionalOptions': [ '/NODEFAULTLIB:MSVCRT' ],
                                    },
                                }
                            }
                        }
                    }
                ]
            ]
        }
    ]
}