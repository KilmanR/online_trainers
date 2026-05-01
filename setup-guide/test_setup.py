#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("=" * 50)
print("Проверка установки Python и пакетов")
print("=" * 50)

# Проверка версии Python
import sys
print(f"\n✅ Python version: {sys.version}")

# Проверка pygame
try:
    import pygame
    print(f"✅ Pygame version: {pygame.ver}")
except ImportError:
    print("❌ Pygame not installed")

# Проверка flask
try:
    import flask
    print(f"✅ Flask version: {flask.__version__}")
except ImportError:
    print("❌ Flask not installed")

# Проверка requests
try:
    import requests
    print(f"✅ Requests version: {requests.__version__}")
except ImportError:
    print("❌ Requests not installed")

print("\n" + "=" * 50)
print("Проверка завершена!")
print("=" * 50)