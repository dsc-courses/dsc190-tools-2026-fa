# Build TikZ figures with latexmk (LuaLaTeX) and rasterize to PNG.
#
# Targets:
#   make              build PNGs for every .tex file in this directory
#   make foo.png      build a single figure
#   make clean        remove _build/ and generated PNGs
#
# Intermediate PDFs and aux files live in _build/; final PNGs sit alongside
# the .tex source so slides.md can reference them directly.

DPI     ?= 300
BUILD   := _build
SOURCES := $(wildcard *.tex)
PNGS    := $(SOURCES:.tex=.png)

# LuaLaTeX (via luaotfload) needs a writable font-cache dir. Nix's default
# TEXMFVAR lives inside the read-only store, so we redirect it into _build/.
export TEXMFVAR := $(CURDIR)/$(BUILD)/texmf-var

.PHONY: all clean
.SECONDARY: $(SOURCES:%.tex=$(BUILD)/%.pdf)

all: $(PNGS)

%.png: $(BUILD)/%.pdf
	pdftoppm -png -r $(DPI) -singlefile $< $*

$(BUILD)/%.pdf: %.tex | $(BUILD)
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=$(BUILD) $<

$(BUILD):
	mkdir -p $(BUILD) $(TEXMFVAR)

clean:
	rm -rf $(BUILD)
	rm -f $(PNGS)
