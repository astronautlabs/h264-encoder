git clone https://github.com/astronautlabs/minih264.git external/minih264
git clone https://github.com/juj/emsdk.git
set EMSCRIPTEN_VERSION=sdk-tag-1.39.15-64bit-upstream

cd emsdk
.\emsdk update-tags
.\emsdk install %EMSCRIPTEN_VERSION%
.\emsdk activate --embedded %EMSCRIPTEN_VERSION%

set EMSDK=/home/user/emsdk
set EMSDK_NODE_BIN=%EMSDK%/node/12.9.1_64bit/bin
set EMSCRIPTEN=%EMSDK%/upstream/emscripten
set PATH=$EMSDK:%EMSCRIPTEN%:%EMSDK_NODE_BIN%:%PATH%
set EM_CONFIG=%EMSDK%/.emscripten
set EM_PORTS=%EMSDK%/.emscripten_ports
set EM_CACHE=%EMSDK%/.emscripten_cache
set EMSDK_NODE=%EMSDK_NODE_BIN%/node
set EMCC_WASM_BACKEND=1
set EMCC_SKIP_SANITY_CHECK=1

mkdir embuild 
cd embuild
cmake -DCMAKE_TOOLCHAIN_FILE=%EMSCRIPTEN%/cmake/Modules/Platform/Emscripten.cmake ..
cmake --build --parallel .
cd ..
npm run build