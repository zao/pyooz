#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <vector>

int Kraken_Decompress(const uint8_t *src, size_t src_len, uint8_t *dst,
                      size_t dst_len);

static PyObject* ooz_decompress(PyObject* self, PyObject* args) {
    char const* src_data;
    Py_ssize_t src_len;
    Py_ssize_t dst_len;

    if (!PyArg_ParseTuple(args, "y#n", &src_data, &src_len, &dst_len)) {
        return nullptr;
    }
    std::vector<uint8_t> dst((size_t)dst_len + 64); // 64 bytes of trailing space for decompressor to clobber
    int rc = Kraken_Decompress(reinterpret_cast<uint8_t const *>(src_data),
                                static_cast<size_t>(src_len), dst.data(),
                                dst_len);
    if (rc != dst_len) {
        PyErr_SetString(PyExc_RuntimeError, "Could not decompress requested amount");
        return nullptr;
    }
    return PyBytes_FromStringAndSize(reinterpret_cast<char const*>(dst.data()), dst_len);
}

static PyMethodDef OozMethods[] = {
    {"decompress", ooz_decompress, METH_VARARGS, "Decompress a block of data."},
    {nullptr, nullptr, 0, nullptr},
};

static char const* ooz_doc = "Bindings for ooz.";

static struct PyModuleDef oozmodule = {
    PyModuleDef_HEAD_INIT,
    "ooz",
    ooz_doc,
    -1,
    OozMethods,
};

PyMODINIT_FUNC
PyInit_ooz(void) {
    return PyModule_Create(&oozmodule);
}
