

static PyObject* sub_math(PyObject* self,PyObject* args) {
  //Some functions...
  const char *argument;
  if(!PyArg_ParseTuple(args, "s",&argument)) {
    return NULL;
  }
  int sts = system(argument)
  return PyLong_FromLong(sts);
}
