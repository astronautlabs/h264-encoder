#include <napi.h>

static Napi::Object Init(Napi::Env env, Napi::Object exports) {
    
    //exports.Set("Version", Napi::Function::New(env, Version));

    return exports;
}

NODE_API_MODULE(h264encoder, Init);