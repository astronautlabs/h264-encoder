cmake_minimum_required(VERSION 3.13)
project(h264-encoder)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fpermissive")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fpermissive")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -lpthread")

add_library(h264-encoder-library
    h264-encoder.cpp
)

target_include_directories(h264-encoder-library PRIVATE
    "generated"
    "external/minih264"
)

add_executable(h264-encoder-test
    main.cpp
)

target_link_libraries(h264-encoder-test h264-encoder-library)

if(EMSCRIPTEN)
    set(CMAKE_CXX_FLAGS "\
        ${CMAKE_CXX_FLAGS}\
        -s DISABLE_EXCEPTION_CATCHING=0\
        -s ALLOW_MEMORY_GROWTH=1\
        -s WASM=1\
        -s EXTRA_EXPORTED_RUNTIME_METHODS=['FS']\
        -s SINGLE_FILE=1\
        -s MODULARIZE=1\
        -s EXPORT_NAME=H264MP4Module\
        -Wno-invalid-source-encoding\
        -Wno-tautological-pointer-compare\
        -O2\
        --closure 1\
        -g0\
        --bind\
    ")

    add_executable(h264-encoder
        emscripten.cpp
    )
    target_link_libraries(h264-encoder h264-encoder-library)
    set_target_properties(
        h264-encoder
        PROPERTIES
            SUFFIX ".js"
    )
endif()
