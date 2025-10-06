# Makefile pour les exercices C
# Compilateur et options
CC = gcc
CFLAGS = -Wall -Wextra -Werror -std=c99 -pedantic -O2
DEBUG_FLAGS = -g -DDEBUG
RELEASE_FLAGS = -O3 -DNDEBUG

# Dossiers
SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
INC_DIR = include

# Créer les dossiers s'ils n'existent pas
DIRS = $(OBJ_DIR) $(BIN_DIR) $(SRC_DIR) $(INC_DIR)

# Sources et objets (exclure les fichiers sans main)
SOURCES = $(wildcard $(SRC_DIR)/*.c)
MAIN_SOURCES = $(filter-out $(SRC_DIR)/math_utils.c, $(SOURCES))
OBJECTS = $(SOURCES:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
TARGETS = $(MAIN_SOURCES:$(SRC_DIR)/%.c=$(BIN_DIR)/%)

# Règle par défaut
all: $(DIRS) $(TARGETS)

# Créer les dossiers
$(DIRS):
	@mkdir -p $@

# Compilation des objets
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@echo "Compilation de $<"
	$(CC) $(CFLAGS) -I$(INC_DIR) -c $< -o $@

# Compilation des exécutables
$(BIN_DIR)/%: $(OBJ_DIR)/%.o $(OBJ_DIR)/math_utils.o
	@echo "Linking $@"
	$(CC) $^ -o $@

# Version debug
debug: CFLAGS += $(DEBUG_FLAGS)
debug: all

# Version release
release: CFLAGS += $(RELEASE_FLAGS)
release: all

# Nettoyage
clean:
	@echo "Nettoyage des fichiers générés"
	@rm -rf $(OBJ_DIR) $(BIN_DIR)

# Nettoyage complet (y compris les exécutables)
distclean: clean
	@rm -rf $(BIN_DIR)

# Installation des dépendances (si nécessaire)
install-deps:
	@echo "Vérification des dépendances système"
	@which gcc > /dev/null || (echo "GCC non trouvé. Installation..." && xcode-select --install)

# Test de compilation
test: all
	@echo "Tests de compilation réussis"
	@echo "Exécutables disponibles:"
	@ls -la $(BIN_DIR)/

# Aide
help:
	@echo "Makefile pour les exercices C"
	@echo ""
	@echo "Commandes disponibles:"
	@echo "  make          - Compilation standard"
	@echo "  make debug    - Compilation avec debug"
	@echo "  make release  - Compilation optimisée"
	@echo "  make clean    - Nettoyage des fichiers générés"
	@echo "  make test     - Test de compilation"
	@echo "  make help     - Afficher cette aide"
	@echo ""
	@echo "Structure:"
	@echo "  src/     - Fichiers sources (.c)"
	@echo "  include/ - Fichiers d'en-tête (.h)"
	@echo "  obj/     - Fichiers objets (.o)"
	@echo "  bin/     - Exécutables"

# Règles spéciales pour les exercices
exo1: $(BIN_DIR)/exo1_hello
exo2: $(BIN_DIR)/exo2_calculator
exo3: $(BIN_DIR)/exo3_arrays

# Phony targets
.PHONY: all clean distclean test help debug release install-deps exo1 exo2 exo3
