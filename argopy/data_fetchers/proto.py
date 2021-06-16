from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import xarray


class ArgoDataFetcherProto(ABC):
    @abstractmethod
    def to_xarray(self) -> xarray.Dataset:
        pass

    @abstractmethod
    def filter_data_mode(self, ds: xarray.Dataset) -> xarray.Dataset:
        pass

    @abstractmethod
    def filter_qc(self, ds: xarray.Dataset) -> xarray.Dataset:
        pass

    @abstractmethod
    def filter_variables(self, ds: xarray.Dataset, mode: str) -> xarray.Dataset:
        pass

    def clear_cache(self):
        """ Remove cache files and entries from resources opened with this fetcher """
        return self.fs.clear_cache()

    def _format(self, x, typ: str) -> str:
        """ string formatting helper """
        if typ == "lon":
            if x < 0:
                x = 360.0 + x
            return ("%05d") % (x * 100.0)
        if typ == "lat":
            return ("%05d") % (x * 100.0)
        if typ == "prs":
            return ("%05d") % (np.abs(x) * 10.0)
        if typ == "tim":
            return pd.to_datetime(x).strftime("%Y-%m-%d")
        return str(x)

    def _cname(self) -> str:
        """ Fetcher one line string definition helper """
        cname = "?"

        if hasattr(self, "BOX"):
            BOX = self.BOX
            cname = ("[x=%0.2f/%0.2f; y=%0.2f/%0.2f]") % (
                BOX[0],
                BOX[1],
                BOX[2],
                BOX[3],
            )
            if len(BOX) == 6:
                cname = ("[x=%0.2f/%0.2f; y=%0.2f/%0.2f; z=%0.1f/%0.1f]") % (
                    BOX[0],
                    BOX[1],
                    BOX[2],
                    BOX[3],
                    BOX[4],
                    BOX[5],
                )
            if len(BOX) == 8:
                cname = ("[x=%0.2f/%0.2f; y=%0.2f/%0.2f; z=%0.1f/%0.1f; t=%s/%s]") % (
                    BOX[0],
                    BOX[1],
                    BOX[2],
                    BOX[3],
                    BOX[4],
                    BOX[5],
                    self._format(BOX[6], "tim"),
                    self._format(BOX[7], "tim"),
                )

        elif hasattr(self, "WMO"):
            prtcyc = lambda f, wmo: "WMO%i_%s" % (
                wmo,
                "_".join(["CYC%i" % (cyc) for cyc in sorted(f.CYC)]),
            )
            if len(self.WMO) == 1:
                if hasattr(self, "CYC") and isinstance(self.CYC, (np.ndarray)):
                    cname = prtcyc(self, self.WMO[0])
                else:
                    cname = "WMO%i" % (self.WMO[0])
            else:
                cname = ";".join(["WMO%i" % wmo for wmo in sorted(self.WMO)])
                if hasattr(self, "CYC") and isinstance(self.CYC, (np.ndarray)):
                    cname = ";".join([prtcyc(self, wmo) for wmo in self.WMO])
            if hasattr(self, "dataset_id"):
                cname = self.dataset_id + ";" + cname

        return cname
