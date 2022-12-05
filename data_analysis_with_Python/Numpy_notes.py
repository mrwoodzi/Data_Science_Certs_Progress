{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7a8d7e67-a576-49eb-b981-fd0b9e32d5cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "cc9e4962-df48-4f15-a2d5-9db3a4e206eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([1, 2, 3, 4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c824c747-aa48-41fd-953f-ba694d0c8b93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d006eec8-861a-495c-b4f7-ac73bd1ba085",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4,)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f2042f9b-27a3-49d1-b4c6-6cdf364cf5a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "b = np.array([0, .5, 1, 1.5, 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2f6e40b4-b142-477c-9268-cfed8c6af02f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5,)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "f475f5e1-dce0-4d1f-9435-8258ca5b77de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.size"
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
   "execution_count": 15,
   "id": "48930fa6-8823-4abe-bdcc-b1e025200e3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.0, 1.0, 2.0)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b[0], b[2], b[-1] ## meaning that you can index at any point, sweet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1037b41c-bf76-467b-b4e4-81b19add5727",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0., 1., 2.])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b[[0, 2, -1]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21c9b6c4-43b8-4a3b-9fb2-d224c900b468",
   "metadata": {},
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
   "cell_type": "markdown",
   "id": "1ea2d613-7b23-4d79-97ac-5ec835fcd81e",
   "metadata": {},
   "source": [
    "Dimensions and Shapes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "21fa623c-e8c3-4030-aba8-e0fe51913278",
   "metadata": {},
   "outputs": [],
   "source": [
    "A = np.array([[1, 2, 3], [4, 5, 6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e0972c64-92a3-412e-87f7-8eb1bb949907",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "5c4c6779-5bb5-4ff5-b95d-a710c3d06721",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "474261b8-9f93-4337-a281-46d03af393c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "812228af-51fe-4828-b94c-ad363a560d01",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "04b412f8-ae21-4f3a-bb3e-fb177d84c6c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 4)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "badfad4f-667e-409b-9e81-26148213ea34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fdb185e-706d-4e4d-a5db-f587de40d7cc",
   "metadata": {},
   "source": [
    "Can have a 3 dimensional Array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "d5af871c-be66-4755-baa2-527236b1aba1",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "square_matrix = np.array([[1, 2, 3,],\n",
    "                          [4, 5, 6], \n",
    "                          [7, 8, 9]\n",
    "                         ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "e09e3a3a-0e00-4364-bf77-75e611397506",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[4, 5],\n",
       "       [7, 8]])"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square_matrix[1:, :2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "3af447f2-33e5-446b-8de5-9c7748cfe8e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [4, 5],\n",
       "       [7, 8]])"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square_matrix[:, :2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "4c3260d7-a05a-426d-8e26-28e068f658fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([12, 15, 18])"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square_matrix.sum(axis=0) ## Axis is the y/frontback"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "c28531dc-c1bf-4c9d-9a85-90b84bfcf527",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "45"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square_matrix.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32117330-8e0b-49bc-8635-8133b2bc426d",
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
