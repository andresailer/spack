# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import sys


class Xsdk(BundlePackage):
    """Xsdk is a suite of Department of Energy (DOE) packages for numerical
       simulation. This is a Spack bundle package that installs the xSDK
       packages
    """

    homepage = "http://xsdk.info"

    maintainers = ['balay', 'luszczek']

    version('develop')
    version('0.5.0')
    version('0.4.0')
    version('0.3.0')
    version('xsdk-0.2.0')

    variant('debug', default=False, description='Compile in debug mode')
    variant('cuda', default=False, description='Enable CUDA dependent packages')
    variant('trilinos', default=True, description='Enable trilinos package build')
    variant('omega-h', default=True, description='Enable omega-h package build')
    variant('strumpack', default=True, description='Enable strumpack package build')
    variant('dealii', default=True, description='Enable dealii package build')
    variant('phist', default=True, description='Enable phist package build')
    variant('ginkgo', default=True, description='Enable ginkgo package build')
    variant('libensemble', default=True, description='Enable py-libensemble package build')
    variant('precice', default=(sys.platform != 'darwin'),
            description='Enable precice package build')
    variant('butterflypack', default=True, description='Enable butterflypack package build')

    depends_on('hypre@develop+superlu-dist+shared', when='@develop')
    depends_on('hypre@2.18.2+superlu-dist+shared', when='@0.5.0')
    depends_on('hypre@2.15.1~internal-superlu', when='@0.4.0')
    depends_on('hypre@2.12.1~internal-superlu', when='@0.3.0')
    depends_on('hypre@xsdk-0.2.0~internal-superlu', when='@xsdk-0.2.0')

    depends_on('mfem@develop+mpi+superlu-dist+petsc~sundials+examples+miniapps', when='@develop')
    depends_on('mfem@4.0.1-xsdk+mpi~superlu-dist+petsc+sundials+examples+miniapps', when='@0.5.0')
    depends_on('mfem@3.4.0+mpi+superlu-dist+petsc+sundials+examples+miniapps', when='@0.4.0')
    depends_on('mfem@3.3.2+mpi+superlu-dist+petsc+sundials+examples+miniapps', when='@0.3.0')

    depends_on('superlu-dist@develop', when='@develop')
    depends_on('superlu-dist@6.1.1', when='@0.5.0')
    depends_on('superlu-dist@6.1.0', when='@0.4.0')
    depends_on('superlu-dist@5.2.2', when='@0.3.0')
    depends_on('superlu-dist@xsdk-0.2.0', when='@xsdk-0.2.0')

    depends_on('trilinos@develop+hypre+superlu-dist+metis+hdf5~mumps+boost~suite-sparse+tpetra+nox+ifpack2+zoltan2+amesos2~exodus+dtk+intrepid2+shards',
               when='@develop +trilinos')
    depends_on('trilinos@12.18.1+hypre+superlu-dist+metis+hdf5~mumps+boost~suite-sparse+tpetra+nox+ifpack2+zoltan2+amesos2~exodus+dtk+intrepid2+shards',
               when='@0.5.0 +trilinos')
    depends_on('trilinos@12.14.1+hypre+superlu-dist+metis+hdf5~mumps+boost~suite-sparse+tpetra+nox+ifpack2+zoltan2+amesos2~exodus+dtk+intrepid2+shards',
               when='@0.4.0 +trilinos')
    depends_on('trilinos@12.12.1+hypre+superlu-dist+metis+hdf5~mumps+boost~suite-sparse~tpetra~ifpack2~zoltan2~amesos2~exodus',
               when='@0.3.0 +trilinos')
    depends_on('trilinos@xsdk-0.2.0+hypre+superlu-dist+metis+hdf5~mumps+boost~suite-sparse~tpetra~ifpack2~zoltan2~amesos2~exodus',
               when='@xsdk-0.2.0 +trilinos')

    depends_on('petsc +trilinos', when='+trilinos')
    depends_on('petsc ~trilinos', when='~trilinos')
    depends_on('petsc +batch', when='platform=cray @0.5.0:')
    depends_on('petsc@develop+mpi+hypre+superlu-dist+metis+hdf5~mumps+double~int64',
               when='@develop')
    depends_on('petsc@3.12.1+mpi+hypre+superlu-dist+metis+hdf5~mumps+double~int64',
               when='@0.5.0')
    depends_on('petsc@3.10.3+mpi+hypre+superlu-dist+metis+hdf5~mumps+double~int64',
               when='@0.4.0')
    depends_on('petsc@3.8.2+mpi+hypre+superlu-dist+metis+hdf5~mumps+double~int64',
               when='@0.3.0')
    depends_on('petsc@xsdk-0.2.0+mpi+hypre+superlu-dist+metis+hdf5~mumps+double~int64',
               when='@xsdk-0.2.0')

    depends_on('dealii +trilinos', when='+trilinos +dealii')
    depends_on('dealii ~trilinos', when='~trilinos +dealii')
    depends_on('dealii@develop~assimp~python~doc~gmsh+petsc+slepc+mpi~int64+hdf5~netcdf+metis~sundials~ginkgo~symengine', when='@develop +dealii')
    depends_on('dealii@9.1.1~assimp~python~doc~gmsh+petsc+slepc+mpi~int64+hdf5~netcdf+metis~sundials~ginkgo~symengine', when='@0.5.0 +dealii')
    depends_on('dealii@9.0.1~assimp~python~doc~gmsh+petsc~slepc+mpi~int64+hdf5~netcdf+metis~ginkgo~symengine', when='@0.4.0 +dealii')

    depends_on('pflotran@develop', when='@develop')
    depends_on('pflotran@xsdk-0.5.0', when='@0.5.0')
    depends_on('pflotran@xsdk-0.4.0', when='@0.4.0')
    depends_on('pflotran@xsdk-0.3.0', when='@0.3.0')
    depends_on('pflotran@xsdk-0.2.0', when='@xsdk-0.2.0')

    depends_on('alquimia@develop', when='@develop')
    depends_on('alquimia@xsdk-0.5.0', when='@0.5.0')
    depends_on('alquimia@xsdk-0.4.0', when='@0.4.0')
    depends_on('alquimia@xsdk-0.3.0', when='@0.3.0')
    depends_on('alquimia@xsdk-0.2.0', when='@xsdk-0.2.0')

    depends_on('sundials+superlu-dist', when='@0.5.0: %gcc@6.1:')
    depends_on('sundials@develop~int64+hypre+petsc', when='@develop')
    depends_on('sundials@5.0.0~int64+hypre+petsc', when='@0.5.0')
    depends_on('sundials@3.2.1~int64+hypre', when='@0.4.0')
    depends_on('sundials@3.1.0~int64+hypre', when='@0.3.0')

    depends_on('plasma@19.8.1:', when='@develop %gcc@6.0:')
    depends_on('plasma@19.8.1:', when='@0.5.0 %gcc@6.0:')
    depends_on('plasma@18.11.1:', when='@0.4.0 %gcc@6.0:')

    depends_on('magma@2.5.1', when='@develop +cuda')
    depends_on('magma@2.5.1', when='@0.5.0 +cuda')
    depends_on('magma@2.4.0', when='@0.4.0 +cuda')
    depends_on('magma@2.2.0', when='@0.3.0 +cuda')

    depends_on('amrex@develop', when='@develop %intel')
    depends_on('amrex@develop', when='@develop %gcc')
    depends_on('amrex@19.08', when='@0.5.0 %intel')
    depends_on('amrex@19.08', when='@0.5.0 %gcc')
    depends_on('amrex@18.10.1', when='@0.4.0 %intel')
    depends_on('amrex@18.10.1', when='@0.4.0 %gcc')

    depends_on('slepc@develop', when='@develop')
    depends_on('slepc@3.12.0', when='@0.5.0')
    depends_on('slepc@3.10.1', when='@0.4.0')

    depends_on('omega-h +trilinos', when='+trilinos +omega-h')
    depends_on('omega-h ~trilinos', when='~trilinos +omega-h')
    depends_on('omega-h@develop', when='@develop +omega-h')
    depends_on('omega-h@9.29.0', when='@0.5.0 +omega-h')
    depends_on('omega-h@9.19.1', when='@0.4.0 +omega-h')

    depends_on('strumpack@master', when='@develop +strumpack')
    depends_on('strumpack@3.3.0', when='@0.5.0 +strumpack')
    depends_on('strumpack@3.1.1', when='@0.4.0 +strumpack')

    depends_on('pumi@develop', when='@develop')
    depends_on('pumi@2.2.1', when='@0.5.0')
    depends_on('pumi@2.2.0', when='@0.4.0')

    tasmanian_openmp = '~openmp' if sys.platform == 'darwin' else '+openmp'
    depends_on('tasmanian@develop+xsdkflags+blas' + tasmanian_openmp, when='@develop')
    depends_on('tasmanian@develop+xsdkflags+blas+cuda+magma' + tasmanian_openmp, when='@develop +cuda')
    depends_on('tasmanian@7.0+xsdkflags+mpi+blas' + tasmanian_openmp, when='@0.5.0')
    depends_on('tasmanian@7.0+xsdkflags+mpi+blas+cuda+magma' + tasmanian_openmp, when='@0.5.0 +cuda')
    depends_on('tasmanian@6.0+xsdkflags+blas~openmp', when='@0.4.0')
    depends_on('tasmanian@6.0+xsdkflags+blas+cuda+magma~openmp', when='@0.4.0 +cuda')

    # the Fortran 2003 bindings of phist require python@3:, but this
    # creates a conflict with other packages like petsc@develop. Actually
    # these are type='build' dependencies, but spack reports a conflict anyway.
    # This will be fixed once the new concretizer becomes available
    # (says @adamjstewart)

    depends_on('phist kernel_lib=tpetra', when='+trilinos +phist')
    depends_on('phist kernel_lib=petsc', when='~trilinos +phist')
    depends_on('phist@develop ~fortran ~scamac ~openmp ~host', when='@develop +phist')
    depends_on('phist@1.8.0 ~fortran ~scamac ~openmp ~host', when='@0.5.0 +phist')
    depends_on('phist@1.7.5 ~fortran ~scamac ~openmp ~host', when='@0.4.0 +phist')

    depends_on('ginkgo@develop ~openmp', when='@develop +ginkgo')
    depends_on('ginkgo@develop ~openmp+cuda', when='@develop +ginkgo +cuda')
    depends_on('ginkgo@1.1.0 ~openmp', when='@0.5.0 +ginkgo')
    depends_on('ginkgo@1.1.0 ~openmp+cuda', when='@0.5.0 +cuda +ginkgo')

    depends_on('py-libensemble@develop+petsc4py', type='run', when='@develop +libensemble')
    depends_on('py-libensemble@0.5.2+petsc4py', type='run', when='@0.5.0 +libensemble')
    depends_on('py-petsc4py@3.12.0', type='run', when='@0.5.0 +libensemble')

    depends_on('precice ~petsc', when='platform=cray +precice')
    depends_on('precice@develop', when='@develop +precice')
    depends_on('precice@1.6.1', when='@0.5.0 +precice')

    depends_on('butterflypack@master', when='@develop +butterflypack')
    depends_on('butterflypack@1.1.0', when='@0.5.0 +butterflypack')

    # xSDKTrilinos depends on the version of Trilinos built with
    # +tpetra which is turned off for faster xSDK
    # depends_on('xsdktrilinos@xsdk-0.2.0', when='@xsdk-0.2.0')
    # depends_on('xsdktrilinos@develop', when='@develop')

    # How do we propagate debug flag to all depends on packages ?
    # If I just do spack install xsdk+debug will that propogate it down?
