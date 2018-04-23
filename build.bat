@echo off

echo Data: 100 26 2
python simulate.py 100 26 2 output/species_100_26_2.data
python trace.py output/species_100_26_2.data output/hist_100_26_2.data output/gens_100_26_2.data
python genhtml.py output/species_100_26_2.data output/gens_100_26_2.data output/index_100_26_2.html index.rtl

echo Data: 100 26 3
python simulate.py 100 26 3 output/species_100_26_3.data
python trace.py output/species_100_26_3.data output/hist_100_26_3.data output/gens_100_26_3.data
python genhtml.py output/species_100_26_3.data output/gens_100_26_3.data output/index_100_26_3.html index.rtl
echo Data: 100 26 4
python simulate.py 100 26 4 output/species_100_26_4.data
python trace.py output/species_100_26_4.data output/hist_100_26_4.data output/gens_100_26_4.data
python genhtml.py output/species_100_26_4.data output/gens_100_26_4.data output/index_100_26_4.html index.rtl
echo Data: 100 26 5
python simulate.py 100 26 5 output/species_100_26_5.data
python trace.py output/species_100_26_5.data output/hist_100_26_5.data output/gens_100_26_5.data
python genhtml.py output/species_100_26_5.data output/gens_100_26_5.data output/index_100_26_5.html index.rtl
echo Data: 100 26 10
python simulate.py 100 26 10 output/species_100_26_10.data
python trace.py output/species_100_26_10.data output/hist_100_26_10.data output/gens_100_26_10.data
python genhtml.py output/species_100_26_10.data output/gens_100_26_10.data output/index_100_26_10.html index.rtl
echo Data: 100 26 20
python simulate.py 100 26 20 output/species_100_26_20.data
python trace.py output/species_100_26_20.data output/hist_100_26_20.data output/gens_100_26_20.data
python genhtml.py output/species_100_26_20.data output/gens_100_26_20.data output/index_100_26_20.html index.rtl
echo Data: 100 10 2
python simulate.py 100 10 2 output/species_100_10_2.data
python trace.py output/species_100_10_2.data output/hist_100_10_2.data output/gens_100_10_2.data
python genhtml.py output/species_100_10_2.data output/gens_100_10_2.data output/index_100_10_2.html index.rtl
echo Data: 100 10 3
python simulate.py 100 10 3 output/species_100_10_3.data
python trace.py output/species_100_10_3.data output/hist_100_10_3.data output/gens_100_10_3.data
python genhtml.py output/species_100_10_3.data output/gens_100_10_3.data output/index_100_10_3.html index.rtl
echo Data: 100 10 4
python simulate.py 100 10 4 output/species_100_10_4.data
python trace.py output/species_100_10_4.data output/hist_100_10_4.data output/gens_100_10_4.data
python genhtml.py output/species_100_10_4.data output/gens_100_10_4.data output/index_100_10_4.html index.rtl
echo Data: 100 10 5
python simulate.py 100 10 5 output/species_100_10_5.data
python trace.py output/species_100_10_5.data output/hist_100_10_5.data output/gens_100_10_5.data
python genhtml.py output/species_100_10_5.data output/gens_100_10_5.data output/index_100_10_5.html index.rtl
echo Data: 100 10 10
python simulate.py 100 10 10 output/species_100_10_10.data
python trace.py output/species_100_10_10.data output/hist_100_10_10.data output/gens_100_10_10.data
python genhtml.py output/species_100_10_10.data output/gens_100_10_10.data output/index_100_10_10.html index.rtl
echo Data: 100 10 20
python simulate.py 100 10 20 output/species_100_10_20.data
python trace.py output/species_100_10_20.data output/hist_100_10_20.data output/gens_100_10_20.data
python genhtml.py output/species_100_10_20.data output/gens_100_10_20.data output/index_100_10_20.html index.rtl
echo on
