# Makefile pour TP Factorielle C
# Compilateur et options
CC = gcc
CFLAGS = -Wall -Wextra -Werror -std=c99 -pedantic -O2
DEBUG_FLAGS = -g -DDEBUG
RELEASE_FLAGS = -O3 -DNDEBUG

# Dossiers
SRC_DIR = .
BIN_DIR = bin
OBJ_DIR = obj

# Créer les dossiers s'ils n'existent pas
DIRS = $(OBJ_DIR) $(BIN_DIR)

# Sources et objets
SOURCES = fact.c bench_fact.c fact_lib.c
OBJECTS = $(SOURCES:%.c=$(OBJ_DIR)/%.o)

# Règle par défaut
all: $(DIRS) $(BIN_DIR)/fact $(BIN_DIR)/bench_fact

# Créer les dossiers
$(DIRS):
	@mkdir -p $@

# Compilation des objets
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@echo "Compilation de $<"
	$(CC) $(CFLAGS) -c $< -o $@

# Exécutable fact (seul)
$(BIN_DIR)/fact: $(OBJ_DIR)/fact.o
	@echo "Linking $@"
	$(CC) $< -o $@

# Exécutable bench_fact (a besoin de fact_lib.o aussi)
$(BIN_DIR)/bench_fact: $(OBJ_DIR)/bench_fact.o $(OBJ_DIR)/fact_lib.o
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

# Nettoyage complet
distclean: clean
	@rm -rf $(BIN_DIR)

# Test de compilation
test: all
	@echo "Tests de compilation réussis"
	@echo "Exécutables disponibles:"
	@ls -la $(BIN_DIR)/

# Exécution des tests
run: all
	@echo "=== Exécution de fact ==="
	@./$(BIN_DIR)/fact 10
	@echo ""
	@echo "=== Exécution de bench_fact ==="
	@./$(BIN_DIR)/bench_fact

# Règles spéciales pour les exercices
fact: $(BIN_DIR)/fact
bench: $(BIN_DIR)/bench_fact

# Aide
help:
	@echo "Makefile pour TP Factorielle C"
	@echo ""
	@echo "Commandes disponibles:"
	@echo "  make          - Compilation standard"
	@echo "  make debug    - Compilation avec debug"
	@echo "  make release  - Compilation optimisée"
	@echo "  make clean    - Nettoyage des fichiers générés"
	@echo "  make test     - Test de compilation"
	@echo "  make run      - Compilation et exécution"
	@echo "  make fact     - Compiler seulement fact"
	@echo "  make bench    - Compiler seulement bench_fact"
	@echo "  make help     - Afficher cette aide"

# Phony targets
.PHONY: all clean distclean test run fact bench help debug release