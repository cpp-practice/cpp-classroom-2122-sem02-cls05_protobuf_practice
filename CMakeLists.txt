cmake_minimum_required(VERSION 3.19)
project(template_repo)

set(CMAKE_CXX_STANDARD 20)

find_package(Protobuf REQUIRED)
include_directories(${PROTOBUF_INCLUDE_DIRS})
add_executable(add-student add_student.cpp student.pb.cc)
target_link_libraries(add-student ${Protobuf_LIBRARIES})