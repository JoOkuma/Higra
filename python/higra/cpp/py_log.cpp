//
// Created by perretb on 28/05/18.
//

#include "py_log.hpp"
#include "py_common.hpp"
#include "higra/detail/log.hpp"


void py_init_log(pybind11::module &m) {


    m.def("set_trace", [](bool enabled) { hg::logger::trace_enabled() = enabled; },
          "Define if function call tracing is enabled.",
          pybind11::arg("enabled"));

    m.def("get_trace", []() { return hg::logger::trace_enabled(); },
          "Get the state of function call tracing.");

    /*m.def("add_logger_callback",
    [](std::function<void(const std::string &)>  fun){
        hg::logger::callbacks().push_back(fun);
        },
    "Add a new callback for Higra logger.",
    pybind11::arg("callback"));*/


    m.def("logger_register_print_callback",
          []() {
              hg::logger::callbacks().push_back([](const std::string &msg) {
                  pybind11::object buildins = pybind11::module::import("builtins");
                  pybind11::object print = buildins.attr("print");
                  print(msg);
              });
          },
          "Register the builtin print function as a logger output."
    );

}
