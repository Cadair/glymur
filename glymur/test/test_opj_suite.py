"""
The tests defined here roughly correspond to what is in the OpenJPEG test
suite.
"""
import re
import sys
import unittest
import warnings

import numpy as np

import glymur
from glymur import Jp2k
from glymur.jp2box import FileTypeBox, ImageHeaderBox, ColourSpecificationBox

from .fixtures import (OPJ_DATA_ROOT, MetadataBase,
                       WARNING_INFRASTRUCTURE_ISSUE,
                       WARNING_INFRASTRUCTURE_MSG,
                       mse, peak_tolerance, read_pgx, opj_data_file,
                       OPENJPEG_NOT_AVAILABLE, OPENJPEG_NOT_AVAILABLE_MSG)


@unittest.skipIf(OPENJPEG_NOT_AVAILABLE, OPENJPEG_NOT_AVAILABLE_MSG)
@unittest.skipIf(OPJ_DATA_ROOT is None,
                 "OPJ_DATA_ROOT environment variable not set")
class TestSuite(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ETS_C1P0_p0_01_j2k(self):
        jfile = opj_data_file('input/conformance/p0_01.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_01_0.pgx')
        pgxdata = read_pgx(pgxfile)

        np.testing.assert_array_equal(jpdata, pgxdata)

    def test_ETS_C1P0_p0_03_j2k(self):
        jfile = opj_data_file('input/conformance/p0_03.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_03_0.pgx')
        pgxdata = read_pgx(pgxfile)

        np.testing.assert_array_equal(jpdata, pgxdata)

    def test_ETS_C1P0_p0_04_j2k(self):
        jfile = opj_data_file('input/conformance/p0_04.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_04_0.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[:, :, 0], pgxdata) < 5)
        self.assertTrue(mse(jpdata[:, :, 0], pgxdata) < 0.776)

        pgxfile = opj_data_file('baseline/conformance/c1p0_04_1.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[:, :, 1], pgxdata) < 4)
        self.assertTrue(mse(jpdata[:, :, 1], pgxdata) < 0.626)

        pgxfile = opj_data_file('baseline/conformance/c1p0_04_2.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[:, :, 2], pgxdata) < 6)
        self.assertTrue(mse(jpdata[:, :, 2], pgxdata) < 1.07)

    def test_ETS_C1P0_p0_08_j2k(self):
        jfile = opj_data_file('input/conformance/p0_08.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[::2, ::2]

        pgxfile = opj_data_file('baseline/conformance/c1p0_08_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 0], pgxdata)

        pgxfile = opj_data_file('baseline/conformance/c1p0_08_1.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 1], pgxdata)

        pgxfile = opj_data_file('baseline/conformance/c1p0_08_2.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 2], pgxdata)

    def test_ETS_C1P0_p0_09_j2k(self):
        jfile = opj_data_file('input/conformance/p0_09.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_09_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata, pgxdata)

    def test_ETS_C1P0_p0_11_j2k(self):
        jfile = opj_data_file('input/conformance/p0_11.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_11_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata, pgxdata)

    def test_ETS_C1P0_p0_14_j2k(self):
        jfile = opj_data_file('input/conformance/p0_14.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_14_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 0], pgxdata)

        pgxfile = opj_data_file('baseline/conformance/c1p0_14_1.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 1], pgxdata)

        pgxfile = opj_data_file('baseline/conformance/c1p0_14_2.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 2], pgxdata)

    def test_ETS_C1P0_p0_15_j2k(self):
        jfile = opj_data_file('input/conformance/p0_15.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_15_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata, pgxdata)

    def test_ETS_C1P0_p0_16_j2k(self):
        jfile = opj_data_file('input/conformance/p0_16.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_16_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata, pgxdata)

    def test_ETS_C1P1_p1_01_j2k(self):
        jfile = opj_data_file('input/conformance/p1_01.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p1_01_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata, pgxdata)

    def test_ETS_C1P1_p1_02_j2k(self):
        jfile = opj_data_file('input/conformance/p1_02.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p1_02_0.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[:, :, 0], pgxdata) < 5)
        self.assertTrue(mse(jpdata[:, :, 0], pgxdata) < 0.765)

        pgxfile = opj_data_file('baseline/conformance/c1p1_02_1.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[:, :, 1], pgxdata) < 4)
        self.assertTrue(mse(jpdata[:, :, 1], pgxdata) < 0.616)

        pgxfile = opj_data_file('baseline/conformance/c1p1_02_2.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[:, :, 2], pgxdata) < 6)
        self.assertTrue(mse(jpdata[:, :, 2], pgxdata) < 1.051)

    def test_ETS_C1P1_p1_04_j2k(self):
        jfile = opj_data_file('input/conformance/p1_04.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p1_04_0.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata, pgxdata) < 624)
        self.assertTrue(mse(jpdata, pgxdata) < 3080)


@unittest.skipIf(OPJ_DATA_ROOT is None,
                 "OPJ_DATA_ROOT environment variable not set")
@unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
class TestSuiteWarns(MetadataBase):
    """
    Identical setup to above, but these tests issue warnings.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ETS_JP2_file2(self):
        jfile = opj_data_file('input/conformance/file2.jp2')
        with self.assertWarns(UserWarning):
            jp2k = Jp2k(jfile)
        jpdata = jp2k[:]
        self.assertEqual(jpdata.shape, (640, 480, 3))

    @unittest.skipIf(glymur.version.openjpeg_version_tuple[0] < 2,
                     "Functionality not implemented for 1.x")
    def test_ETS_JP2_file3(self):
        jfile = opj_data_file('input/conformance/file3.jp2')
        with self.assertWarns(UserWarning):
            jp2k = Jp2k(jfile)
        jpdata = jp2k.read_bands()
        self.assertEqual(jpdata[0].shape, (640, 480))
        self.assertEqual(jpdata[1].shape, (320, 240))
        self.assertEqual(jpdata[2].shape, (320, 240))

    def test_ETS_JP2_file4(self):
        jfile = opj_data_file('input/conformance/file4.jp2')
        with self.assertWarns(UserWarning):
            jp2k = Jp2k(jfile)
        jpdata = jp2k[:]
        self.assertEqual(jpdata.shape, (512, 768))

    def test_ETS_JP2_file5(self):
        jfile = opj_data_file('input/conformance/file5.jp2')
        with self.assertWarns(UserWarning):
            # There's a warning for an unknown compatibility entry.
            # Ignore it here.
            jp2k = Jp2k(jfile)
        jpdata = jp2k[:]
        self.assertEqual(jpdata.shape, (512, 768, 3))

    def test_ETS_JP2_file6(self):
        jfile = opj_data_file('input/conformance/file6.jp2')
        with self.assertWarns(UserWarning):
            jp2k = Jp2k(jfile)
        jpdata = jp2k[:]
        self.assertEqual(jpdata.shape, (512, 768))

    def test_ETS_JP2_file7(self):
        jfile = opj_data_file('input/conformance/file7.jp2')
        with self.assertWarns(UserWarning):
            jp2k = Jp2k(jfile)
        jpdata = jp2k[:]
        self.assertEqual(jpdata.shape, (640, 480, 3))

    def test_ETS_JP2_file8(self):
        jfile = opj_data_file('input/conformance/file8.jp2')
        with self.assertWarns(UserWarning):
            jp2k = Jp2k(jfile)
        jpdata = jp2k[:]
        self.assertEqual(jpdata.shape, (400, 700))

    def test_ETS_JP2_file9(self):
        jfile = opj_data_file('input/conformance/file9.jp2')
        with self.assertWarns(UserWarning):
            jp2k = Jp2k(jfile)
        jpdata = jp2k[:]
        self.assertEqual(jpdata.shape, (512, 768, 3))

    def test_NR_broken1_jp2_dump(self):
        jfile = opj_data_file('input/nonregression/broken1.jp2')

        # The colr box has a ridiculously incorrect box length.
        regex = re.compile(r'''b'colr'\sbox\shas\sincorrect\sbox\slength\s
                               \(\d+\)''',
                           re.VERBOSE)
        with self.assertWarnsRegex(UserWarning, regex):
            jp2 = Jp2k(jfile)

        ids = [box.box_id for box in jp2.box]
        self.assertEqual(ids, ['jP  ', 'ftyp', 'jp2h', 'jp2c'])

        ids = [box.box_id for box in jp2.box[2].box]
        self.assertEqual(ids, ['ihdr', 'colr'])

        # Signature box.  Check for corruption.
        self.assertEqual(jp2.box[0].signature, (13, 10, 135, 10))
        self.verify_filetype_box(jp2.box[1], FileTypeBox())

        expected = ImageHeaderBox(152, 203, num_components=3)
        self.verifyImageHeaderBox(jp2.box[2].box[0], expected)

        expected = ColourSpecificationBox(colorspace=glymur.core.SRGB)
        self.verifyColourSpecificationBox(jp2.box[2].box[1], expected)

        c = jp2.box[3].codestream

        ids = [x.marker_id for x in c.segment]
        expected = ['SOC', 'SIZ', 'CME', 'COD', 'QCD', 'QCC', 'QCC']
        self.assertEqual(ids, expected)

        kwargs = {'rsiz': 0, 'xysiz': (203, 152), 'xyosiz': (0, 0),
                  'xytsiz': (203, 152), 'xytosiz': (0, 0),
                  'bitdepth': (8, 8, 8),
                  'signed': (False, False, False),
                  'xyrsiz': [(1, 1, 1), (1, 1, 1)]}
        self.verifySizSegment(c.segment[1],
                              glymur.codestream.SIZsegment(**kwargs))

        pargs = (glymur.core.RCME_ISO_8859_1,
                 "Creator: JasPer Version 1.701.0".encode())
        self.verifyCMEsegment(c.segment[2],
                              glymur.codestream.CMEsegment(*pargs))

        # COD: Coding style default
        self.assertFalse(c.segment[3].scod & 2)  # no sop
        self.assertFalse(c.segment[3].scod & 4)  # no eph
        self.assertEqual(c.segment[3].spcod[0], glymur.core.LRCP)
        self.assertEqual(c.segment[3].layers, 1)  # layers = 1
        self.assertEqual(c.segment[3].spcod[3], 1)  # mct
        self.assertEqual(c.segment[3].spcod[4], 5)  # level
        self.assertEqual(tuple(c.segment[3].code_block_size),
                         (64, 64))  # cblk
        self.verify_codeblock_style(c.segment[3].spcod[7],
                                    [False, False, False, False, False, False])
        self.assertEqual(c.segment[3].spcod[8],
                         glymur.core.WAVELET_XFORM_5X3_REVERSIBLE)
        self.assertEqual(len(c.segment[3].spcod), 9)

        # QCD: Quantization default
        self.assertEqual(c.segment[4].sqcd & 0x1f, 0)
        self.assertEqual(c.segment[4].guard_bits, 2)
        self.assertEqual(c.segment[4].mantissa, [0] * 16)
        self.assertEqual(c.segment[4].exponent,
                         [8] + [9, 9, 10] * 5)

        # QCC: Quantization component
        # associated component
        self.assertEqual(c.segment[5].cqcc, 1)
        self.assertEqual(c.segment[5].guard_bits, 2)
        # quantization type
        self.assertEqual(c.segment[5].sqcc & 0x1f, 0)  # none
        self.assertEqual(c.segment[5].mantissa, [0] * 16)
        self.assertEqual(c.segment[5].exponent,
                         [8] + [9, 9, 10] * 5)

        # QCC: Quantization component
        # associated component
        self.assertEqual(c.segment[6].cqcc, 2)
        self.assertEqual(c.segment[6].guard_bits, 2)
        # quantization type
        self.assertEqual(c.segment[6].sqcc & 0x1f, 0)  # none
        self.assertEqual(c.segment[6].mantissa, [0] * 16)
        self.assertEqual(c.segment[6].exponent,
                         [8] + [9, 9, 10] * 5)


@unittest.skipIf(OPJ_DATA_ROOT is None,
                 "OPJ_DATA_ROOT environment variable not set")
@unittest.skipIf(glymur.version.openjpeg_version_tuple[0] != 2,
                 "Feature not supported in glymur until openjpeg 2.0")
class TestSuiteBands(unittest.TestCase):
    """
    Test the read_bands method.
    """
    def test_ETS_C1P1_p1_03_j2k(self):
        jfile = opj_data_file('input/conformance/p1_03.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k.read_bands()

        pgxfile = opj_data_file('baseline/conformance/c1p1_03_0.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[0], pgxdata) < 2)
        self.assertTrue(mse(jpdata[0], pgxdata) < 0.3)

        pgxfile = opj_data_file('baseline/conformance/c1p1_03_1.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[1], pgxdata) < 2)
        self.assertTrue(mse(jpdata[1], pgxdata) < 0.21)

        pgxfile = opj_data_file('baseline/conformance/c1p1_03_2.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[2], pgxdata) <= 1)
        self.assertTrue(mse(jpdata[2], pgxdata) < 0.2)

        pgxfile = opj_data_file('baseline/conformance/c1p1_03_3.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[3], pgxdata)

    def test_ETS_C1P0_p0_05_j2k(self):
        jfile = opj_data_file('input/conformance/p0_05.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k.read_bands()

        pgxfile = opj_data_file('baseline/conformance/c1p0_05_0.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[0], pgxdata) < 2)
        self.assertTrue(mse(jpdata[0], pgxdata) < 0.302)

        pgxfile = opj_data_file('baseline/conformance/c1p0_05_1.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[1], pgxdata) < 2)
        self.assertTrue(mse(jpdata[1], pgxdata) < 0.307)

        pgxfile = opj_data_file('baseline/conformance/c1p0_05_2.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[2], pgxdata) < 2)
        self.assertTrue(mse(jpdata[2], pgxdata) < 0.269)

        pgxfile = opj_data_file('baseline/conformance/c1p0_05_3.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[3], pgxdata) == 0)
        self.assertTrue(mse(jpdata[3], pgxdata) == 0)

    def test_ETS_C1P0_p0_06_j2k(self):
        jfile = opj_data_file('input/conformance/p0_06.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k.read_bands()

        pgxfile = opj_data_file('baseline/conformance/c1p0_06_0.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[0], pgxdata) < 635)
        self.assertTrue(mse(jpdata[0], pgxdata) < 11287)

        pgxfile = opj_data_file('baseline/conformance/c1p0_06_1.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[1], pgxdata) < 403)
        self.assertTrue(mse(jpdata[1], pgxdata) < 6124)

        pgxfile = opj_data_file('baseline/conformance/c1p0_06_2.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[2], pgxdata) < 378)
        self.assertTrue(mse(jpdata[2], pgxdata) < 3968)

        pgxfile = opj_data_file('baseline/conformance/c1p0_06_3.pgx')
        pgxdata = read_pgx(pgxfile)
        self.assertTrue(peak_tolerance(jpdata[3], pgxdata) == 0)
        self.assertTrue(mse(jpdata[3], pgxdata) == 0)

    def test_NR_DEC_merged_jp2_19_decode(self):
        jfile = opj_data_file('input/nonregression/merged.jp2')
        Jp2k(jfile).read_bands()
        self.assertTrue(True)


@unittest.skipIf(OPJ_DATA_ROOT is None,
                 "OPJ_DATA_ROOT environment variable not set")
@unittest.skipIf(glymur.version.openjpeg_version_tuple[0] < 2,
                 "Tests not passing until 2.0")
class TestSuite2point0(unittest.TestCase):
    """Runs tests introduced in version 2.0 or that pass only in 2.0"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ETS_C1P0_p0_10_j2k(self):
        jfile = opj_data_file('input/conformance/p0_10.j2k')
        jp2k = Jp2k(jfile)
        jpdata = jp2k[:]

        pgxfile = opj_data_file('baseline/conformance/c1p0_10_0.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 0], pgxdata)

        pgxfile = opj_data_file('baseline/conformance/c1p0_10_1.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 1], pgxdata)

        pgxfile = opj_data_file('baseline/conformance/c1p0_10_2.pgx')
        pgxdata = read_pgx(pgxfile)
        np.testing.assert_array_equal(jpdata[:, :, 2], pgxdata)

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_broken2_jp2_5_decode(self):
        """
        Invalid marker ID on codestream, Null pointer access upon read.
        """
        jfile = opj_data_file('input/nonregression/broken2.jp2')
        regex = re.compile(r'''Invalid\smarker\sid\sencountered\sat\sbyte\s
                               \d+\sin\scodestream:\s*"0x[a-fA-F0-9]{4}"''',
                           re.VERBOSE)
        with self.assertRaises(IOError):
            with self.assertWarnsRegex(UserWarning, regex):
                Jp2k(jfile)[:]

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_broken4_jp2_7_decode(self):
        jfile = opj_data_file('input/nonregression/broken4.jp2')
        with self.assertRaises(IOError):
            with self.assertWarns(UserWarning):
                # invalid number of subbands, bad marker ID
                Jp2k(jfile)[:]
        self.assertTrue(True)

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_kakadu_v4_4_openjpegv2_broken_j2k_16_decode(self):
        # This test actually passes in 1.5, but produces unpleasant warning
        # messages that cannot be turned off?
        relpath = 'input/nonregression/kakadu_v4-4_openjpegv2_broken.j2k'
        jfile = opj_data_file(relpath)
        if glymur.version.openjpeg_version_tuple[0] < 2:
            with self.assertWarns(UserWarning):
                # Incorrect warning issued about tile parts.
                Jp2k(jfile)[:]
        else:
            Jp2k(jfile)[:]
        self.assertTrue(True)


@unittest.skipIf(OPJ_DATA_ROOT is None,
                 "OPJ_DATA_ROOT environment variable not set")
@unittest.skipIf(re.match(r'''0|1|2.0.0''',
                          glymur.version.openjpeg_version) is not None,
                 "Only supported in 2.0.1 or higher")
class TestSuite2point1(unittest.TestCase):
    """Runs tests introduced in version 2.0+ or that pass only in 2.0+"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_NR_DEC_gdal_fuzzer_unchecked_num_resolutions_jp2_36_decode(self):
        f = 'input/nonregression/gdal_fuzzer_unchecked_numresolutions.jp2'
        jfile = opj_data_file(f)
        with self.assertWarns(UserWarning):
            # Invalid number of resolutions.
            j = Jp2k(jfile)
            with self.assertRaises(IOError):
                j[:]

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_gdal_fuzzer_check_number_of_tiles_jp2_38_decode(self):
        relpath = 'input/nonregression/gdal_fuzzer_check_number_of_tiles.jp2'
        jfile = opj_data_file(relpath)
        with self.assertWarns(UserWarning):
            # Invalid number of tiles.
            j = Jp2k(jfile)
            with self.assertRaises(IOError):
                j[:]

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_gdal_fuzzer_check_comp_dx_dy_jp2_39_decode(self):
        relpath = 'input/nonregression/gdal_fuzzer_check_comp_dx_dy.jp2'
        jfile = opj_data_file(relpath)
        with self.assertWarns(UserWarning):
            # Invalid subsampling value
            with self.assertRaises(IOError):
                Jp2k(jfile)[:]

    def test_NR_DEC_file_409752_jp2_40_decode(self):
        jfile = opj_data_file('input/nonregression/file409752.jp2')
        with self.assertRaises(RuntimeError):
            Jp2k(jfile)[:]

    def test_NR_DEC_issue206_image_000_jp2_42_decode(self):
        jfile = opj_data_file('input/nonregression/issue206_image-000.jp2')
        Jp2k(jfile)[:]
        self.assertTrue(True)

    def test_NR_DEC_p1_04_j2k_57_decode(self):
        jfile = opj_data_file('input/conformance/p1_04.j2k')
        jp2k = Jp2k(jfile)
        tdata = jp2k[896:1024, 896:1024]  # last tile
        odata = jp2k[:]
        np.testing.assert_array_equal(tdata, odata[896:1024, 896:1024])

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_p1_04_j2k_57_decode_0p7_backwards_compatibility(self):
        """
        0.7.x usage deprecated
        """
        jfile = opj_data_file('input/conformance/p1_04.j2k')
        jp2k = Jp2k(jfile)
        if sys.hexversion < 0x03000000:
            with warnings.catch_warnings():
                # Suppress a warning due to deprecated syntax
                warnings.simplefilter("ignore")
                tdata = jp2k.read(tile=63)  # last tile
        else:
            with self.assertWarns(DeprecationWarning):
                tdata = jp2k.read(tile=63)  # last tile
        odata = jp2k[:]
        np.testing.assert_array_equal(tdata, odata[896:1024, 896:1024])

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_p1_04_j2k_58_decode_0p7_backwards_compatibility(self):
        """
        0.7.x usage deprecated
        """
        jfile = opj_data_file('input/conformance/p1_04.j2k')
        jp2k = Jp2k(jfile)
        if sys.hexversion < 0x03000000:
            with warnings.catch_warnings():
                # Suppress a warning due to deprecated syntax
                tdata = jp2k.read(tile=63, rlevel=2)  # last tile
        else:
            with self.assertWarns(DeprecationWarning):
                tdata = jp2k.read(tile=63, rlevel=2)  # last tile
        odata = jp2k[::4, ::4]
        np.testing.assert_array_equal(tdata, odata[224:256, 224:256])

    def test_NR_DEC_p1_04_j2k_58_decode(self):
        jfile = opj_data_file('input/conformance/p1_04.j2k')
        jp2k = Jp2k(jfile)
        tdata = jp2k[896:1024:4, 896:1024:4]  # last tile
        odata = jp2k[::4, ::4]
        np.testing.assert_array_equal(tdata, odata[224:256, 224:256])

    def test_NR_DEC_p1_04_j2k_59_decode(self):
        jfile = opj_data_file('input/conformance/p1_04.j2k')
        jp2k = Jp2k(jfile)
        tdata = jp2k[128:256, 512:640]  # 2nd row, 5th column
        odata = jp2k[:]
        np.testing.assert_array_equal(tdata, odata[128:256, 512:640])

    def test_NR_DEC_p1_04_j2k_60_decode(self):
        jfile = opj_data_file('input/conformance/p1_04.j2k')
        jp2k = Jp2k(jfile)
        tdata = jp2k[128:256:2, 512:640:2]  # 2nd row, 5th column
        odata = jp2k[::2, ::2]
        np.testing.assert_array_equal(tdata, odata[64:128, 256:320])

    @unittest.skipIf(WARNING_INFRASTRUCTURE_ISSUE, WARNING_INFRASTRUCTURE_MSG)
    def test_NR_DEC_jp2_36_decode(self):
        lst = ('input',
               'nonregression',
               'gdal_fuzzer_assert_in_opj_j2k_read_SQcd_SQcc.patch.jp2')
        jfile = opj_data_file('/'.join(lst))
        with self.assertWarns(UserWarning):
            # Invalid component number.
            j = Jp2k(jfile)
            with self.assertRaises(IOError):
                j[:]
