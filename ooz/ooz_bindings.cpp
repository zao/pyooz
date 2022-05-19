#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

int Kraken_Decompress(const uint8_t *src, size_t src_len, uint8_t *dst,
                      size_t dst_len);

namespace py = pybind11;

PYBIND11_MODULE(ooz, m) {
  m.doc() = "Bindings for ooz.";
  m.def(
      "decompress",
      [](py::bytes const &src, int dst_len) -> py::bytes {
        py::buffer_info info = py::buffer(src).request();
        std::vector<uint8_t> dst(
            (size_t)dst_len +
            64); // 64 bytes of trailing space for decompressor to clobber
        int rc = Kraken_Decompress(reinterpret_cast<uint8_t const *>(info.ptr),
                                   static_cast<size_t>(info.size), dst.data(),
                                   dst_len);
        if (rc != dst_len) {
          throw std::runtime_error("Could not decompress requested amount");
        }
        return py::bytes(reinterpret_cast<char const *>(dst.data()), dst_len);
      },
      py::arg("src"), py::arg("dst_len"));
}