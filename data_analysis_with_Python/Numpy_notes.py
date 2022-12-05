{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7a8d7e67-a576-49eb-b981-fd0b9e32d5cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0104cf8-2191-4509-b382-2d428dcabfa7",
   "metadata": {},
   "source": [
    "np.array([1, 2, 3, 4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cc9e4962-df48-4f15-a2d5-9db3a4e206eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([1, 2, 3, 4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f2042f9b-27a3-49d1-b4c6-6cdf364cf5a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "b = np.array([0, .5, 1, 1.5, 2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1f64d64-7d0d-4276-8a20-f83966bca7e6",
   "metadata": {},
   "source": [
    "Below is **multi indexing**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48930fa6-8823-4abe-bdcc-b1e025200e3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "b[0], b[2], b[-1] ## meaning that you can index at any point, sweet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1037b41c-bf76-467b-b4e4-81b19add5727",
   "metadata": {},
   "outputs": [],
   "source": [
    "b[[0, 2, -1]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2942f454-6fac-48e7-a7a8-65a5a894be84",
   "metadata": {},
   "outputs": [],
   "source": [
    "Both above are multi indexing"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4e488a4-22bf-494f-ac08-57d5a6b7e580",
   "metadata": {},
   "source": [
    "Different Array Types:\n",
    "can identify with variable.dtype\n",
    "you can also specify type of int via"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c86da848-a599-4626-8636-8d3b63c8489a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'a' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43ma\u001b[49m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'a' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21fa623c-e8c3-4030-aba8-e0fe51913278",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "vscode": {
   "interpreter": {
    "hash": "9e3a5b40f939a4ff757e3f5a32cd7a4e978076baaabe8d49d5793491c50a6746"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
