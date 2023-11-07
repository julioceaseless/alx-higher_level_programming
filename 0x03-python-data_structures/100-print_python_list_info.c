#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints the information of
 * a python list object
 * @p: pointer to a python object
 * Return: Nothing!
 */
void print_python_list_info(PyObject *p)
{
	py_ssize_t size, i;

	if (!PyList_Check(p))
		return;

	size = PyList_Size(p);
	printf("The size of the Python List: %ld\n", PyList_Size(p));
	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		if (PyUnicode_Check(item))
		{
			printf("Element %ld: %s\n", i, PyUnicode_AsUTF8(item));
		}
		else if (PyInt_Check(item))
		{
			long value = PyInt_AsLong(item);

			printf("Element %ld: %ld\n", i, value);
		}
		else if (PyFloat_Check(item))
		{
			double value = PyFloat_AsDouble(item);

			printf("Element %ld: %f\n", i, value);
		}
		else
		{
			printf("Element %ld: <unknown type>\n", i);
		}
	}
}

