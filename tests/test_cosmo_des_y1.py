from copy import deepcopy

from test_cosmo_planck_2015 import params_lowTEB_highTTTEEE
from common_cosmo import body_of_test

best_fit = deepcopy(params_lowTEB_highTTTEEE)
camb_extra = {"halofit_version": "mead"}
classy_extra = {"non linear": "hmcode"}


def test_cosmo_des_y1_shear_camb(modules):
    like = "des_y1_shear"
    info_likelihood = {like: {}}
    best_fit_shear = deepcopy(best_fit)
    best_fit_shear.update(test_params_shear)
    info_theory = {"camb": {"extra_args": camb_extra}}
    body_of_test(modules, best_fit_shear, info_likelihood, info_theory,
                 {like: ref_chi2["shear"], "tolerance": tolerance})


def test_cosmo_des_y1_clustering_camb(modules):
    like = "des_y1_clustering"
    info_likelihood = {like: {}}
    best_fit_clustering = deepcopy(best_fit)
    best_fit_clustering.update(test_params_clustering)
    info_theory = {"camb": {"extra_args": camb_extra}}
    body_of_test(modules, best_fit_clustering, info_likelihood, info_theory,
                 {like: ref_chi2["clustering"], "tolerance": tolerance})


def test_cosmo_des_y1_galaxy_galaxy_camb(modules):
    like = "des_y1_galaxy_galaxy"
    info_likelihood = {like: {}}
    best_fit_galaxy_galaxy = deepcopy(best_fit)
    best_fit_galaxy_galaxy.update(test_params_shear)
    best_fit_galaxy_galaxy.update(test_params_clustering)
    info_theory = {"camb": {"extra_args": camb_extra}}
    body_of_test(modules, best_fit_galaxy_galaxy, info_likelihood, info_theory,
                 {like: ref_chi2["galaxy_galaxy"], "tolerance": tolerance})


def test_cosmo_des_y1_joint_camb(modules):
    like = "des_y1_joint"
    info_likelihood = {like: {}}
    best_fit_joint = deepcopy(best_fit)
    best_fit_joint.update(test_params_shear)
    best_fit_joint.update(test_params_clustering)
    info_theory = {"camb": {"extra_args": camb_extra}}
    body_of_test(modules, best_fit_joint, info_likelihood, info_theory,
                 {like: ref_chi2["joint"], "tolerance": tolerance})


def test_cosmo_des_y1_shear_classy(modules):
    like = "des_y1_shear"
    info_likelihood = {like: {}}
    best_fit_shear = deepcopy(best_fit)
    best_fit_shear.update(test_params_shear)
    info_theory = {"classy": {"extra_args": classy_extra}}
    body_of_test(modules, best_fit_shear, info_likelihood, info_theory,
                 {like: ref_chi2["shear"], "tolerance": tolerance})


def test_cosmo_des_y1_clustering_classy(modules):
    like = "des_y1_clustering"
    info_likelihood = {like: {}}
    best_fit_clustering = deepcopy(best_fit)
    best_fit_clustering.update(test_params_clustering)
    info_theory = {"classy": {"extra_args": classy_extra}}
    body_of_test(modules, best_fit_clustering, info_likelihood, info_theory,
                 {like: ref_chi2["clustering"], "tolerance": tolerance})


def test_cosmo_des_y1_galaxy_galaxy_classy(modules):
    like = "des_y1_galaxy_galaxy"
    info_likelihood = {like: {}}
    best_fit_galaxy_galaxy = deepcopy(best_fit)
    best_fit_galaxy_galaxy.update(test_params_shear)
    best_fit_galaxy_galaxy.update(test_params_clustering)
    info_theory = {"classy": {"extra_args": classy_extra}}
    body_of_test(modules, best_fit_galaxy_galaxy, info_likelihood, info_theory,
                 {like: ref_chi2["galaxy_galaxy"], "tolerance": tolerance})


ref_chi2 = {"shear": 242.825, "clustering": 100.997,
            "galaxy_galaxy": 208.005, "joint": 570.428}
tolerance = 0.2

test_params_shear = {
    # wl_photoz_errors
    "DES_DzS1": 0.002,
    "DES_DzS2": -0.015,
    "DES_DzS3": 0.007,
    "DES_DzS4": -0.018,
    # shear_calibration_parameters
    "DES_m1": 0.012,
    "DES_m2": 0.012,
    "DES_m3": 0.012,
    "DES_m4": 0.012,
    # Intrinsic Alignment
    "DES_AIA": 1.0,
    "DES_alphaIA": 1.0,
    "DES_z0IA": 0.62}

test_params_clustering = {
    # lens_photoz_errors
    "DES_DzL1": 0.002,
    "DES_DzL2": 0.001,
    "DES_DzL3": 0.003,
    "DES_DzL4": 0,
    "DES_DzL5": 0,
    # bin_bias
    "DES_b1": 1.45,
    "DES_b2": 1.55,
    "DES_b3": 1.65,
    "DES_b4": 1.8,
    "DES_b5": 2.0}
