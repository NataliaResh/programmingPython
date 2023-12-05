#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

typedef struct {
    size_t size;
    double **matrix;
} Matrix;

Matrix zero_matrix(size_t size) {
    Matrix matrix;
    matrix.size = size;
    matrix.matrix = (double**)malloc(sizeof(double*) * size);
    for (size_t i = 0; i < size; i++) {
        matrix.matrix[i] = calloc(size, sizeof(double));
    }
    return matrix;
}

void free_matrix(Matrix *matrix) {
    for (size_t i = 0; i < matrix->size; i++) {
        free(matrix->matrix[i]);
    }
    free(matrix->matrix);
}

Matrix identity_matrix(size_t size) {
    Matrix matrix = zero_matrix(size);
    for (size_t i = 0; i < size; i++) {
        matrix.matrix[i][i] = 1;
    }
    return matrix;
}

Matrix matrix_power(Matrix *matrix, unsigned int pow) {
    Matrix result = identity_matrix(matrix->size);
    for (unsigned int p = 0; p < pow; p++) {
        Matrix powering_matrix = zero_matrix(matrix->size);
        for (size_t i = 0; i < matrix->size; i++) {
            for (size_t j = 0; j < matrix->size; j++) {
                double sum = 0;
                for (size_t k = 0; k < matrix->size; k++) {
                    sum += result.matrix[i][k] * matrix->matrix[k][j];
                }
                powering_matrix.matrix[i][j] = sum;
            }
        }
        free_matrix(&result);
        result = powering_matrix;
    }
    return result;
}

int converter_matrix(PyObject *obj_list, void *address) {
    Matrix *matrix = address;
    size_t size = PyList_Size(obj_list);
    *matrix = zero_matrix(size);
    for (size_t i = 0; i < size; i++) {
        PyObject *list = PyList_GetItem(obj_list, i);
        for (size_t j = 0; j < size; j++) {
            PyObject *elem = PyList_GetItem(list, j);
            matrix->matrix[i][j] = PyFloat_AsDouble(elem);
        }
    }
    return 1;
}

PyObject *c_matrix_to_python(Matrix *matrix) {
    size_t size = matrix->size;
    PyObject *py_matrix = PyList_New(size);
    for (size_t i = 0; i < size; i++) {
        PyObject *item = PyList_New(size);
        for (size_t j = 0; j < size; j++) {
            PyObject *elem = PyFloat_FromDouble(matrix->matrix[i][j]);
            PyList_SetItem(item, j, elem);
        }
        PyList_SetItem(py_matrix, i, item);
    }
    return py_matrix;
}

static PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    Matrix matrix;
    unsigned int pow = 0;
    if (!PyArg_ParseTuple(args, "O&I", converter_matrix, &matrix, &pow)) {
        return NULL;
    }
    Matrix powering_matrix = matrix_power(&matrix, pow);
    PyObject *py_powering_Matrix = c_matrix_to_python(&powering_matrix);
    free_matrix(&matrix);
    free_matrix(&powering_matrix);
    return py_powering_Matrix;
}

static PyMethodDef ForeignMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS,
      "Raises a matrix to a power."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign",
    NULL,
    1,
    ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
  }
