cmake_minimum_required(VERSION 3.6)

project(Maya)

include_directories(F:/a.wendleder/Downloads/MayaDevkit2016/Maya-devkit-master/win/include)
link_directories("E:/Program Files/Autodesk/Maya2016/lib")

set(CMAKE_SHARED_LIBRARY_SUFFIX .mll)
set(CMAKE_SHARED_LINKER_FLAGS "/export:initializePlugin /export:uninitializePlugin")

add_library(Gonzo SHARED Gonzo.cpp)
target_link_libraries(Gonzo Foundation OpenMaya)
