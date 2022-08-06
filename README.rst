vamas
=====

This is a Python library to read `VAMAS`_ files (.vms). [1]_

.. _`VAMAS`: https://doi.org/10.1002/sia.740130202


Installing
----------

Installation via `pip`_:

.. code-block:: bash

    $ pip install vamas

.. _pip: https://pip.pypa.io/en/stable/


Example Usage
-------------

.. code-block:: python
    
  from vamas import Vamas


  vamas_data = Vamas('path/to/vamas-file.vms')


The created object has two attributes, ``header`` and ``blocks``, which are
instances of ``VamasHeader`` and a list of ``VamasBlock``, respectively.
See the `documentation`_ for all attributes of those classes.

.. _`documentation`: https://matkrin.github.io/vamas

|

----

.. [1] W. A. Dench, L. B. Hazell, M. P. Seah, *Surf. Interface Anal.* **1988**,
  *13*, 63-122.
  `<https://doi.org/10.1002/sia.740130202>`_
